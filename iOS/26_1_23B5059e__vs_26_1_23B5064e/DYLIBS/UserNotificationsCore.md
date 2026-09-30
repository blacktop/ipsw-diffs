## UserNotificationsCore

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore`

```diff

-640.1.16.100.0
-  __TEXT.__text: 0x18f06c
-  __TEXT.__auth_stubs: 0x3320
-  __TEXT.__objc_methlist: 0x788c
+640.1.19.0.0
+  __TEXT.__text: 0x18f75c
+  __TEXT.__auth_stubs: 0x3370
+  __TEXT.__objc_methlist: 0x7894
   __TEXT.__cstring: 0xd973
   __TEXT.__const: 0xd228
   __TEXT.__gcc_except_tab: 0x784
-  __TEXT.__oslogstring: 0xcfc8
+  __TEXT.__oslogstring: 0xd058
   __TEXT.__dlopen_cstrs: 0xf4
   __TEXT.__constg_swiftt: 0x59bc
   __TEXT.__swift5_typeref: 0x52e4

   __TEXT.__swift5_capture: 0x16f8
   __TEXT.__swift_as_ret: 0x150
   __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__unwind_info: 0x54b8
+  __TEXT.__unwind_info: 0x54c0
   __TEXT.__eh_frame: 0x59a0
   __TEXT.__objc_classname: 0xe9a
-  __TEXT.__objc_methname: 0x161d4
-  __TEXT.__objc_methtype: 0x313c
+  __TEXT.__objc_methname: 0x1620c
+  __TEXT.__objc_methtype: 0x3188
   __TEXT.__objc_stubs: 0xd680
   __DATA_CONST.__got: 0x1168
-  __DATA_CONST.__const: 0x1528
+  __DATA_CONST.__const: 0x1520
   __DATA_CONST.__objc_classlist: 0x610
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x2d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4620
+  __DATA_CONST.__objc_selrefs: 0x4628
   __DATA_CONST.__objc_protorefs: 0x168
   __DATA_CONST.__objc_superrefs: 0x1f0
-  __AUTH_CONST.__auth_got: 0x19a0
+  __AUTH_CONST.__auth_got: 0x19c8
   __AUTH_CONST.__const: 0xa378
   __AUTH_CONST.__cfstring: 0x64e0
-  __AUTH_CONST.__objc_const: 0x22040
+  __AUTH_CONST.__objc_const: 0x220c8
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH.__objc_data: 0xd30
   __AUTH.__data: 0x26c0
   __DATA.__objc_ivar: 0x870
-  __DATA.__data: 0x33b8
+  __DATA.__data: 0x33a8
   __DATA.__bss: 0xc3f0
   __DATA.__common: 0xd8
   __DATA_DIRTY.__objc_data: 0x28a8
-  __DATA_DIRTY.__data: 0x5928
+  __DATA_DIRTY.__data: 0x5938
   __DATA_DIRTY.__bss: 0x5280
   __DATA_DIRTY.__common: 0x350
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 97B53516-442D-397F-9E41-A18A79AB0953
-  Functions: 8269
+  UUID: 86297C6D-D4C9-3702-B824-EA29A585E252
+  Functions: 8270
   Symbols:   12374
-  CStrings:  6976
+  CStrings:  6981
 
Symbols:
+ _close
+ _read
- __swift_FORCE_LOAD_$_swiftUIKit
- __swift_FORCE_LOAD_$_swiftUIKit_$_UserNotificationsCore
CStrings:
+ "Failed to close file descriptor for %{private}s. errno: %{public}d"
+ "Failed to read first byte from %{private}s"
+ "First byte of attachment %{private}s: 0x%{private}s"
+ "Unable to open %{private}s. errno: %d"
+ "receiveAttachment(fileURL): %s attachmentIdentifier: %s, notificationIdentifier: %s, bundleIdentifier: %s"
+ "service:account:inviteDroppedForSessionID:fromID:error:"
+ "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48"
- "allAttachmentsAvailable %s file opening error %@"
- "receiveAttachment(fileURL): No attachments - send it on: %s attachmentIdentifier: %s, notificationIdentifier: %s, bundleIdentifier: %s"

```
