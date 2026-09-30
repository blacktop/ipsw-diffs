## CallKit

> `/System/Library/Frameworks/CallKit.framework/CallKit`

```diff

-1367.100.1.0.0
-  __TEXT.__text: 0x67ba0
+1367.100.1.2.1
+  __TEXT.__text: 0x67be0
   __TEXT.__auth_stubs: 0x940
   __TEXT.__objc_methlist: 0x8fd4
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x6258
+  __TEXT.__cstring: 0x626b
   __TEXT.__oslogstring: 0x3694
   __TEXT.__gcc_except_tab: 0x778
-  __TEXT.__unwind_info: 0x1ca0
+  __TEXT.__unwind_info: 0x1cb0
   __TEXT.__objc_classname: 0x1471
-  __TEXT.__objc_methname: 0x119f7
+  __TEXT.__objc_methname: 0x11a5d
   __TEXT.__objc_methtype: 0x3de8
-  __TEXT.__objc_stubs: 0xaa00
+  __TEXT.__objc_stubs: 0xaa20
   __DATA_CONST.__got: 0x4e0
   __DATA_CONST.__const: 0xd40
   __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x33c0
+  __DATA_CONST.__objc_selrefs: 0x33d0
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x370
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x4b0
   __AUTH_CONST.__const: 0x580
-  __AUTH_CONST.__cfstring: 0x4280
-  __AUTH_CONST.__objc_const: 0xebf0
+  __AUTH_CONST.__cfstring: 0x42a0
+  __AUTH_CONST.__objc_const: 0xebd0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x1c20
-  __DATA.__objc_ivar: 0x920
+  __DATA.__objc_ivar: 0x91c
   __DATA.__data: 0x1740
   __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0xb40

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: BC0ED0BE-B3B6-3340-857D-FD3D1DE08063
+  UUID: C1E2B48D-A839-3D70-961C-7A4135E374CD
   Functions: 3177
   Symbols:   10388
-  CStrings:  4682
+  CStrings:  4689
 
Symbols:
+ -[CXSetScreeningCallAction initWithCallUUID:screeningMode:]
+ -[CXSetScreeningCallAction screeningMode]
+ _OBJC_IVAR_$_CXSetScreeningCallAction._screeningMode
+ _objc_msgSend$screeningMode
- -[CXSetScreeningCallAction receptionist]
- -[CXSetScreeningCallAction setReceptionist:]
- _OBJC_IVAR_$_CXSetScreeningCallAction._receptionist
- _OBJC_IVAR_$_CXSetScreeningCallAction._screening
CStrings:
+ " screeningMode=%ld"
+ "TB,N,GisScreening"
+ "Tq,R,N,V_screeningMode"
+ "_screeningMode"
+ "initWithCallUUID:screeningMode:"
+ "screeningMode"

```
