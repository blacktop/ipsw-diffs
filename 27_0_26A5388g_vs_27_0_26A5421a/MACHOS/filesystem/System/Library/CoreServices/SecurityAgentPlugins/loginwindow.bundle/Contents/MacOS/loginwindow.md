## loginwindow

> `/System/Library/CoreServices/SecurityAgentPlugins/loginwindow.bundle/Contents/MacOS/loginwindow`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-396.0.0.0.0
-  __TEXT.__text: 0x272ac
-  __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_stubs: 0x6200
-  __TEXT.__objc_methlist: 0x218c
+399.0.0.0.0
+  __TEXT.__text: 0x27e80
+  __TEXT.__auth_stubs: 0xc90
+  __TEXT.__objc_stubs: 0x6300
+  __TEXT.__objc_methlist: 0x21ec
   __TEXT.__const: 0x6c
-  __TEXT.__gcc_except_tab: 0x4ac
-  __TEXT.__cstring: 0x5c6e
-  __TEXT.__oslogstring: 0x119
-  __TEXT.__objc_methname: 0x5fa5
+  __TEXT.__gcc_except_tab: 0x4b0
+  __TEXT.__cstring: 0x5d59
+  __TEXT.__oslogstring: 0x1c1
+  __TEXT.__objc_methname: 0x6117
   __TEXT.__objc_classname: 0x294
-  __TEXT.__objc_methtype: 0x1224
+  __TEXT.__objc_methtype: 0x1235
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x8f8
+  __TEXT.__unwind_info: 0x918
   __DATA_CONST.__const: 0xa98
-  __DATA_CONST.__cfstring: 0x50a0
+  __DATA_CONST.__cfstring: 0x5140
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_intobj: 0x150
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x650
+  __DATA_CONST.__auth_got: 0x658
   __DATA_CONST.__got: 0x3c8
-  __DATA.__objc_const: 0x1fc0
-  __DATA.__objc_selrefs: 0x1f70
-  __DATA.__objc_ivar: 0x100
+  __DATA.__objc_const: 0x2000
+  __DATA.__objc_selrefs: 0x1fb8
+  __DATA.__objc_ivar: 0x104
   __DATA.__objc_data: 0x500
   __DATA.__data: 0x4e8
   __DATA.__crash_info: 0x148

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcsfde.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 769
-  Symbols:   466
-  CStrings:  2040
+  Functions: 778
+  Symbols:   467
+  CStrings:  2066
 
Symbols:
+ _os_signpost_id_generate
CStrings:
+ "LWUIInit_EFIUser"
+ "LWUIInit_PSSOActivate"
+ "LWUIInit_SetLoginStyle"
+ "LWUIInit_ShowDelay"
+ "LWUIInit_Start"
+ "PSSO submit in flight - not resetting biometry"
+ "PSSO submit in flight for %@"
+ "PSSO submit resolved, clearing submitted user %@"
+ "ShowUI_BuildLoginUI"
+ "ShowUI_BuildUserUI"
+ "ShowUI_MainWork"
+ "ShowUI_SmartCard"
+ "T@\"NSTimer\",&,V_activateUntilFrontmostTimer"
+ "_activateUntilFrontmostTimer"
+ "_setPSSOSubmittedUserName:"
+ "_showNameAndPasswordWithUserName:andPassword:activatePlatformSSO:"
+ "_stopActivateUntilFrontmostTimer"
+ "activateUntilFrontmostTimer"
+ "platformSSOSubmitInFlight"
+ "setActivateUntilFrontmostTimer:"
+ "setWindowLevels:"
+ "showNameAndPasswordWithoutPlatformSSO"
+ "showUserSelectorOrPlatformSSO"
+ "user list is empty and PSSO did not activate, showing name and password"
+ "user list is empty, re-presented PSSO"
+ "v36@0:8@16@24B32"
```
