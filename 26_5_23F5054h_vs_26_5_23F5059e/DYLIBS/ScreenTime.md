## ScreenTime

> `/System/Library/Frameworks/ScreenTime.framework/ScreenTime`

```diff

-605.5.9.0.0
-  __TEXT.__text: 0x49dc
-  __TEXT.__auth_stubs: 0x340
+605.5.10.0.0
+  __TEXT.__text: 0x4a40
+  __TEXT.__auth_stubs: 0x350
   __TEXT.__objc_methlist: 0x71c
   __TEXT.__const: 0x78
   __TEXT.__cstring: 0x2ea
-  __TEXT.__gcc_except_tab: 0xa0
+  __TEXT.__gcc_except_tab: 0xc8
   __TEXT.__oslogstring: 0x4a6
-  __TEXT.__unwind_info: 0x240
-  __TEXT.__objc_classname: 0x102
-  __TEXT.__objc_methname: 0x1644
-  __TEXT.__objc_methtype: 0x538
+  __TEXT.__unwind_info: 0x248
+  __TEXT.__objc_classname: 0x105
+  __TEXT.__objc_methname: 0x1657
+  __TEXT.__objc_methtype: 0x544
   __TEXT.__objc_stubs: 0xfe0
-  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__got: 0x150
   __DATA_CONST.__const: 0x348
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_selrefs: 0x5c0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x1b0
+  __AUTH_CONST.__auth_got: 0x1b8
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x1e0
-  __AUTH_CONST.__objc_const: 0xe60
+  __AUTH_CONST.__objc_const: 0xe80
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x50
+  __DATA.__objc_ivar: 0x54
   __DATA.__data: 0x240
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x10

   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 197F145E-6B77-3357-A69E-2614C0FD8CBD
+  UUID: D6BDD6C5-E2DE-3D01-860F-61D455EAB199
   Functions: 169
-  Symbols:   753
-  CStrings:  359
+  Symbols:   756
+  CStrings:  361
 
Symbols:
+ GCC_except_table14
+ _OBJC_IVAR_$_STScreenTimeConfigurationObserver._configurationLock
+ _objc_alloc_init
Functions:
~ -[STScreenTimeConfigurationObserver initWithUpdateQueue:] : 140 -> 164
~ ___58-[STScreenTimeConfigurationObserver _requestConfiguration]_block_invoke_2 : 148 -> 212
~ -[STScreenTimeConfigurationObserver .cxx_destruct] : 68 -> 80
CStrings:
+ "@\"NSObject\""
+ "_configurationLock"

```
