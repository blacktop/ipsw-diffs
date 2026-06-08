## IOHIDKeyboardFilter

> `/System/Library/HIDPlugins/IOHIDKeyboardFilter.plugin/IOHIDKeyboardFilter`

```diff

-2238.120.5.0.0
-  __TEXT.__text: 0x9460
-  __TEXT.__auth_stubs: 0x760
+2353.0.0.0.1
+  __TEXT.__text: 0x8c7c
   __TEXT.__objc_methlist: 0x94
-  __TEXT.__const: 0x1d0
-  __TEXT.__gcc_except_tab: 0x694
-  __TEXT.__cstring: 0x3ff
-  __TEXT.__oslogstring: 0x4bb
-  __TEXT.__unwind_info: 0x418
-  __TEXT.__objc_classname: 0x2e
-  __TEXT.__objc_methname: 0x1a1
-  __TEXT.__objc_methtype: 0x7a
-  __TEXT.__objc_stubs: 0x1c0
-  __DATA_CONST.__got: 0xe0
+  __TEXT.__const: 0x1cc
+  __TEXT.__gcc_except_tab: 0x63c
+  __TEXT.__cstring: 0x402
+  __TEXT.__oslogstring: 0x563
+  __TEXT.__unwind_info: 0x420
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__objc_selrefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x3c8
+  __DATA_CONST.__got: 0xd0
   __AUTH_CONST.__const: 0x1a8
   __AUTH_CONST.__cfstring: 0x6e0
   __AUTH_CONST.__objc_const: 0x1a8
+  __AUTH_CONST.__weak_auth_got: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x78
   __DATA.__objc_ivar: 0xc

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 59A99435-4C57-3815-AA95-1AEB64735FD0
-  Functions: 193
-  Symbols:   238
-  CStrings:  179
+  UUID: DF11DAC5-3293-3740-947C-BD77E2659E8D
+  Functions: 191
+  Symbols:   243
+  CStrings:  147
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x3
- __ZNSt3__119piecewise_constructE
- _objc_autoreleaseReturnValue
- _objc_retain
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "createMapFromArrayOfPairs: unexpected type for dst key (expected CFNumber, got %@)\n"
+ "createMapFromArrayOfPairs: unexpected type for src key (expected CFNumber, got %@)\n"
- ".cxx_destruct"
- "@\"NSMutableSet\""
- "@16@0:8"
- "@32@0:8^v16^{__IOHIDService=}24"
- "AppleKeyboardStateManager"
- "B24@0:8@16"
- "StickyKeyHandler"
- "StickyKeyNotification:"
- "T@\"NSMutableSet\",&,N,V_capsLockStateTable"
- "^v"
- "^{__IOHIDService=}"
- "_capsLockStateTable"
- "_filter"
- "_service"
- "addObject:"
- "addObserver:selector:name:object:"
- "boolValue"
- "capsLockStateTable"
- "containsObject:"
- "defaultCenter"
- "init"
- "initWithFilter:service:"
- "isCapsLockEnabled:"
- "object"
- "removeObject:"
- "removeObserver"
- "removeObserver:name:object:"
- "setCapsLockEnabled:locationID:"
- "setCapsLockStateTable:"
- "sharedManager"
- "unsignedIntValue"
- "v16@0:8"
- "v24@0:8@16"
- "v28@0:8B16@20"

```
