## RemindersDES

> `/System/Library/DistributedEvaluation/Plugins/RemindersDES.desPlugin/RemindersDES`

```diff

-1170.0.0.0.0
+1202.0.0.0.0
   __TEXT.__text: 0x2bac
   __TEXT.__auth_stubs: 0x5e0
   __TEXT.__objc_methlist: 0x20

   __DATA_CONST.__auth_got: 0x2f0
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__auth_ptr: 0xa0
-  __DATA_CONST.__const: 0x2e0
+  __DATA_CONST.__const: 0x2e8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 65
-  Symbols:   99
+  Symbols:   100
   CStrings:  93
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftOSLog

```
