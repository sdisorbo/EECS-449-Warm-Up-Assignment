from __future__ import annotations
from jaclang.plugin.feature import JacFeature as _Jac
from jaclang.plugin.builtin import *
from dataclasses import dataclass as __jac_dataclass__

@_Jac.make_walker(on_entry=[_Jac.DSFunc('return_message', None)], on_exit=[])
@__jac_dataclass__(eq=False)
class interact(_Jac.Walker):

    def return_message(self, _jac_here_) -> None:
        _Jac.report({'response': 'Hello, world!'})

@_Jac.make_walker(on_entry=[_Jac.DSFunc('return_message', None)], on_exit=[])
@__jac_dataclass__(eq=False)
class interact_with_body(_Jac.Walker):
    name: str

    def return_message(self, _jac_here_) -> None:
        _Jac.report({'response': 'Hello, ' + self.name + '!'})

@_Jac.make_walker(on_entry=[_Jac.DSFunc('return_message', None)], on_exit=[])
@__jac_dataclass__(eq=False)
class interact_with_body_and_query(_Jac.Walker):
    name: str
    age: int

    def return_message(self, _jac_here_) -> None:
        _Jac.report({'response': 'Hello, ' + self.name + '! You are ' + str(self.age) + ' years old.'})

@_Jac.make_walker(on_entry=[_Jac.DSFunc('return_message', None)], on_exit=[])
@__jac_dataclass__(eq=False)
class add_numbers(_Jac.Walker):
    num1: int
    num2: int

    def return_message(self, _jac_here_) -> None:
        _Jac.report({'response': 'The sum is: ' + str(self.num1 + self.num2)})
