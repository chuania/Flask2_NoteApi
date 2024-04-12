from api import app, multi_auth
from api.models.note import NoteModel
from api.models.note import UserModel
from api.schemas.note import NoteSchema, NoteRequestSchema
from utility.helpers import get_object_or_404
from flask_apispec import doc, marshal_with, use_kwargs


@app.route("/notes", methods=["GET"])
@doc(description="Api for notes", tags=["Notes"], summary="Get all quotes")
@marshal_with(NoteSchema(many=True), code=200)
@multi_auth.login_required
def get_notes():
    # Авторизованный пользователь получает только свои заметки
    # и публичные заметки других пользователей
    user = multi_auth.current_user()
    notes = NoteModel.query.join(NoteModel.author).filter(
        (UserModel.id == user.id) | (NoteModel.private == False)
    )
    return notes, 200


@app.route("/notes/<int:note_id>", methods=["GET"])
@doc(description="Api for note", tags=["Notes"], summary="Get note by id")
@marshal_with(NoteSchema, code=200)
@multi_auth.login_required
def get_note_by_id(note_id):
    # Авторизованный пользователь может получить только свою заметку
    # или публичную заметку других пользователей
    # Попытка получить чужую приватную заметку, возвращает ответ с кодом 403
    user = multi_auth.current_user()
    note = get_object_or_404(NoteModel, note_id)
    if not note.private or note.author_id == user.id:
        return note, 200
    else:
        return {"error": "No access"}, 403


@app.route("/notes", methods=["POST"])
@doc(description="Create note", tags=["Notes"], summary="Create note")
@marshal_with(NoteSchema, code=201)
@use_kwargs(NoteRequestSchema, location="json")
@multi_auth.login_required
def create_note(**kwargs):
    user = multi_auth.current_user()
    note = NoteModel(author_id=user.id, **kwargs)
    note.save()
    return note, 201


@app.route("/notes/<int:note_id>", methods=["PUT"])
@doc(description="Edit note", tags=["Notes"], summary="Edit note")
@marshal_with(NoteSchema, code=200)
@use_kwargs(NoteRequestSchema, location="json")
@multi_auth.login_required
def edit_note(note_id, **kwargs):
    # Пользователь может редактировать только свои заметки
    # Попытка редактировать чужую заметку, возвращает ответ с кодом 403
    user = multi_auth.current_user()
    note = get_object_or_404(NoteModel, note_id)
    if user.id == note.author_id:
        for key, value in kwargs.items():
            setattr(note, key, value)
        note.save()
        return note, 200
    return {"error": " not access"}, 403


@app.route("/notes/<int:note_id>", methods=["DELETE"])
@doc(description="Delete note", tags=["Notes"], summary="Delete note")
@multi_auth.login_required
def delete_note(note_id):
    # Пользователь может удалять только свои заметки
    # Попытка удалить чужую заметку, возвращает ответ с кодом 403
    user = multi_auth.current_user()
    note = get_object_or_404(NoteModel, note_id)
    if user.id == note.author_id:
        note.delete()
        return {"message": f"The Note with id {note_id} has deleted"}
    return {"error": " not access"}, 403
