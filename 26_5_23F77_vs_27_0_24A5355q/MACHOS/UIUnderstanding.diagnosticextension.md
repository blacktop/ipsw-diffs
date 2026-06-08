## UIUnderstanding.diagnosticextension

> `/System/Library/PrivateFrameworks/UIUnderstanding.framework/PlugIns/UIUnderstanding.diagnosticextension.appex/UIUnderstanding.diagnosticextension`

```diff

 2.8.0.0.0
-  __TEXT.__text: 0x2a8
-  __TEXT.__auth_stubs: 0x110
+  __TEXT.__text: 0x26c
+  __TEXT.__auth_stubs: 0x120
   __TEXT.__objc_stubs: 0x140
   __TEXT.__objc_methlist: 0x2c
   __TEXT.__const: 0x60

   __TEXT.__objc_methname: 0x14b
   __TEXT.__objc_methtype: 0x13
   __TEXT.__unwind_info: 0x68
-  __DATA_CONST.__auth_got: 0x90
-  __DATA_CONST.__got: 0x28
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x98
+  __DATA_CONST.__got: 0x28
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x60
   __DATA.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 68A0DC86-95B3-3D3C-ABE1-C84F431C6BFD
+  UUID: A62FEDF2-7BD9-3EDA-B4E4-D32F4DBC0857
   Functions: 4
-  Symbols:   34
+  Symbols:   35
   CStrings:  20
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x25
+ _objc_release_x27
+ _objc_retain_x8
- _objc_release_x26
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
Functions:
~ sub_100000ab8 : 516 -> 504
~ sub_100000cc4 -> sub_100000cb8 : 156 -> 108

```
