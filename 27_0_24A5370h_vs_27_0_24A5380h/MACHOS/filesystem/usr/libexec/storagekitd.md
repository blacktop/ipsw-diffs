## storagekitd

> `/usr/libexec/storagekitd`

```diff

-  __TEXT.__text: 0x2cda8
-  __TEXT.__auth_stubs: 0xc40
+  __TEXT.__text: 0x2ce70
+  __TEXT.__auth_stubs: 0xc50
   __TEXT.__objc_stubs: 0x63e0
   __TEXT.__objc_methlist: 0x29a4
   __TEXT.__objc_classname: 0x4f1

   __TEXT.__objc_methtype: 0xfe6
   __TEXT.__const: 0x90
   __TEXT.__gcc_except_tab: 0xb1c
-  __TEXT.__cstring: 0x2ea6
-  __TEXT.__oslogstring: 0x275f
+  __TEXT.__cstring: 0x2ec6
+  __TEXT.__oslogstring: 0x2784
   __TEXT.__unwind_info: 0xaa8
   __DATA_CONST.__const: 0xf60
   __DATA_CONST.__cfstring: 0x1ec0

   __DATA_CONST.__objc_dictobj: 0x1b8
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x630
-  __DATA_CONST.__got: 0x528
+  __DATA_CONST.__auth_got: 0x638
+  __DATA_CONST.__got: 0x568
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x5fc0
   __DATA.__objc_selrefs: 0x1cc0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 922
-  Symbols:   375
-  CStrings:  2417
+  Functions: 923
+  Symbols:   376
+  CStrings:  2419
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _DARegisterExitCallback
CStrings:
+ "%s: Received DA daemon exit callback"
+ "void DaemonExitCallback(void *)"

```
