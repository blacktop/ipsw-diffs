## IOGameControllerFamily

> `/System/Library/Extensions/IOGameControllerFamily.kext/IOGameControllerFamily`

```diff

   __TEXT.__const: 0x480
-  __TEXT.__cstring: 0x101c
-  __TEXT.__os_log: 0x1c4a
-  __TEXT_EXEC.__text: 0x1abac
+  __TEXT.__cstring: 0x104c
+  __TEXT.__os_log: 0x1c18
+  __TEXT_EXEC.__text: 0x1ada8
   __TEXT_EXEC.__auth_stubs: 0x540
   __DATA.__data: 0xc8
   __DATA.__common: 0x290

   __DATA_CONST.__const: 0x5a70
   __DATA_CONST.__kalloc_type: 0x840
   __DATA_CONST.__auth_got: 0x2a0
-  __DATA_CONST.__got: 0xd8
-  Functions: 672
-  Symbols:   914
-  CStrings:  298
+  __DATA_CONST.__got: 0xe0
+  Functions: 673
+  Symbols:   915
+  CStrings:  299
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
Symbols:
+ __ZN17IOHIDEventService9metaClassE
+ __ZN22IOGCDynamicDeviceProbe9preflightEP11IOHIDDevice
- __ZZN22IOGCDynamicDeviceProbe5startEP9IOServiceE11_os_log_fmt_0
CStrings:
+ "GameControllerCategory"
+ "GameControllerEligible"
+ "GameControllerSupport"
- "GameControllerClass"
- "[%#010llx] <IOHIDDevice %#010llx> already probed."

```
