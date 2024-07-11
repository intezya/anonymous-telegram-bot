from aiogram.fsm.state import State, StatesGroup


class UserStates(StatesGroup):
    get_text_to_send: State = State()
