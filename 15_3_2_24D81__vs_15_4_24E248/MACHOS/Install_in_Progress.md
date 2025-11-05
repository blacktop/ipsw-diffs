## Install in Progress

> `/System/Library/CoreServices/Install in Progress.app/Contents/MacOS/Install in Progress`

```diff

-18.0.0.0.0
-  __TEXT.__text: 0x13d0
-  __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__objc_stubs: 0x6c0
-  __TEXT.__objc_methlist: 0x164
-  __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0xa4
-  __TEXT.__cstring: 0x252
-  __TEXT.__objc_methname: 0xd67
+19.0.0.0.0
+  __TEXT.__text: 0x16d4
+  __TEXT.__auth_stubs: 0x250
+  __TEXT.__objc_stubs: 0x7c0
+  __TEXT.__objc_methlist: 0x4b4
+  __TEXT.__const: 0x64
+  __TEXT.__gcc_except_tab: 0xb0
+  __TEXT.__cstring: 0x2db
+  __TEXT.__objc_methname: 0xe88
   __TEXT.__objc_classname: 0x3c
-  __TEXT.__objc_methtype: 0x4fd
-  __TEXT.__unwind_info: 0xb0
-  __DATA_CONST.__auth_got: 0xe0
-  __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0xf0
-  __DATA_CONST.__cfstring: 0x280
+  __TEXT.__objc_methtype: 0x512
+  __TEXT.__unwind_info: 0xb8
+  __DATA_CONST.__auth_got: 0x138
+  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__const: 0x108
+  __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xb50
-  __DATA.__objc_selrefs: 0x218
-  __DATA.__objc_ivar: 0x28
+  __DATA.__objc_const: 0x550
+  __DATA.__objc_selrefs: 0x448
+  __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc0
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/PackageKit.framework/Versions/A/PackageKit
+  - /System/Library/PrivateFrameworks/SoftwareUpdate.framework/Versions/A/SoftwareUpdate
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CE75E88C-F0A4-3787-9C9D-C1E478E78754
-  Functions: 39
-  Symbols:   45
-  CStrings:  261
+  UUID: E0DF96A4-80C3-325E-B523-B7CF3AABAAA7
+  Functions: 43
+  Symbols:   61
+  CStrings:  276
 
Symbols:
+ _CFRelease
+ _CFRetain
+ _FSEventStreamCreate
+ _FSEventStreamInvalidate
+ _FSEventStreamRelease
+ _FSEventStreamSetDispatchQueue
+ _FSEventStreamStart
+ _FSEventStreamStop
+ _OBJC_CLASS_$_NSArray
+ _SULoginWindowCookiePath
+ ___stack_chk_fail
+ ___stack_chk_guard
+ _free
+ _kCFAllocatorDefault
+ _realpath$DARWIN_EXTSN
+ _strcmp
CStrings:
+ "Failed to setup FSEventStreamCreate for SU Post Logout."
+ "Post logout was armed, app will no longer block shutdown/restart."
+ "RestartRequest"
+ "TB,V_softwareUpdatePostLogoutArmed"
+ "Tq,V_action"
+ "_action"
+ "_monitorSoftwareUpdatePostLogout"
+ "_softwareUpdatePostLogoutArmed"
+ "action"
+ "arrayWithObjects:count:"
+ "fileSystemRepresentation"
+ "lastPathComponent"
+ "q"
+ "q16@0:8"
+ "setPreventsApplicationTerminationWhenModal:"
+ "setSoftwareUpdatePostLogoutArmed:"
+ "softwareUpdatePostLogoutArmed"
+ "stringByAppendingPathComponent:"
+ "stringByDeletingLastPathComponent"
+ "v24@0:8q16"
+ "window"
- "T@\"NSString\",&,N,V_actionType"
- "_actionType"
- "actionType"
- "isEqualToString:"
- "setActionType:"

```
