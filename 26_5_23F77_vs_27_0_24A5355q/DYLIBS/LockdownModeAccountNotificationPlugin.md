## LockdownModeAccountNotificationPlugin

> `/System/Library/Accounts/Notification/LockdownModeAccountNotificationPlugin.bundle/LockdownModeAccountNotificationPlugin`

```diff

-80.120.2.0.0
-  __TEXT.__text: 0x6f0
-  __TEXT.__auth_stubs: 0x1d0
+122.0.0.0.0
+  __TEXT.__text: 0x6b8
   __TEXT.__objc_methlist: 0x18c
   __TEXT.__const: 0x90
   __TEXT.__constg_swiftt: 0x58

   __TEXT.__oslogstring: 0x75
   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0x80
-  __TEXT.__objc_classname: 0x59
-  __TEXT.__objc_methname: 0x2ab
-  __TEXT.__objc_methtype: 0x1ff
-  __TEXT.__objc_stubs: 0x80
-  __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0x48
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x110
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__objc_const: 0x1a8
+  __AUTH_CONST.__auth_got: 0xe0
   __AUTH.__objc_data: 0x48
   __DATA.__data: 0xd0
   __DATA.__bss: 0x8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: AFFF9AEA-75E9-3E0D-B974-39F6A22F6CA0
+  UUID: 895D41C8-89FC-39DF-ADEA-4D96E9C75C6A
   Functions: 8
-  Symbols:   42
-  CStrings:  70
+  Symbols:   41
+  CStrings:  5
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio
- _objc_release_x23
- _objc_retain_x24
Functions:
~ sub_2a6f72318 -> sub_23bf2e360 : 1180 -> 1124
CStrings:
- "#16@0:8"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "ACDAccountNotificationPlugin"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"ACAccount\"16@\"ACDAccountStore\"24"
- "B32@0:8@16@24"
- "B40@0:8@\"ACAccount\"16@\"ACDAccountStore\"24^@32"
- "B40@0:8@16@24^@32"
- "B44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "B44@0:8@16i24@28@36"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC37LockdownModeAccountNotificationPlugin6Plugin"
- "account:didChangeWithType:inStore:oldAccount:"
- "account:didPerformActionsForDataclasses:"
- "account:willChangeWithType:inStore:oldAccount:"
- "account:willPerformActionsForDataclasses:"
- "accountType"
- "autorelease"
- "canRemoveAccount:inStore:"
- "canRemoveAccount:inStore:error:"
- "canSaveAccount:inStore:"
- "canSaveAccount:inStore:error:"
- "class"
- "conformsToProtocol:"
- "dealloc"
- "debugDescription"
- "description"
- "hash"
- "identifier"
- "init"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "securityLevelForAccount:"
- "self"
- "sharedInstance"
- "superclass"
- "v32@0:8@\"ACAccount\"16@\"NSArray\"24"
- "v32@0:8@16@24"
- "v44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "v44@0:8@16i24@28@36"
- "zone"

```
