## libedit.3.dylib

> `/usr/lib/libedit.3.dylib`

```diff

-62.0.0.0.0
-  __TEXT.__text: 0x156b8
-  __TEXT.__auth_stubs: 0x720
+65.0.0.0.0
+  __TEXT.__text: 0x15730
+  __TEXT.__auth_stubs: 0x730
   __TEXT.__const: 0x6452
-  __TEXT.__cstring: 0xe01
+  __TEXT.__cstring: 0xe34
   __TEXT.__unwind_info: 0x4e0
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x1330
-  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__auth_got: 0x398
   __AUTH_CONST.__const: 0x3b0
   __DATA.__data: 0x85
   __DATA.__bss: 0xe28

   __DATA_DIRTY.__common: 0x10
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libncurses.5.4.dylib
-  UUID: 115B00C9-6657-3383-8215-A8D5497D072A
+  UUID: B7C7BCA8-0AAC-3B39-B75D-FAD166B32DFD
   Functions: 421
-  Symbols:   270
-  CStrings:  287
+  Symbols:   271
+  CStrings:  289
 
Symbols:
+ _memmove
Functions:
~ sub_2199af27c -> sub_219d3127c : 1160 -> 1232
~ sub_2199afe48 -> sub_219d31e90 : 204 -> 240
~ _history_expand : 3212 -> 3224
CStrings:
+ "%ls: instring too long.\n"
+ "%ls: outstring too long.\n"

```
