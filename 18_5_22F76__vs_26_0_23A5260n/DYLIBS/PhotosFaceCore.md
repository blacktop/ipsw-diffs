## PhotosFaceCore

> `/System/Library/PrivateFrameworks/PhotosFaceCore.framework/PhotosFaceCore`

```diff

-79.1.0.0.0
-  __TEXT.__text: 0x379c
+93.0.0.0.0
+  __TEXT.__text: 0x3928
   __TEXT.__auth_stubs: 0x2f0
-  __TEXT.__objc_methlist: 0x4bc
+  __TEXT.__objc_methlist: 0x504
   __TEXT.__const: 0x2a2
-  __TEXT.__cstring: 0x2fe
+  __TEXT.__cstring: 0x33e
   __TEXT.__oslogstring: 0x43f
   __TEXT.__swift5_typeref: 0x17
   __TEXT.__constg_swiftt: 0x38

   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0x120
-  __TEXT.__objc_classname: 0x96
-  __TEXT.__objc_methname: 0x1036
+  __TEXT.__objc_classname: 0x97
+  __TEXT.__objc_methname: 0x10ec
   __TEXT.__objc_methtype: 0x240
-  __TEXT.__objc_stubs: 0xca0
+  __TEXT.__objc_stubs: 0xd00
   __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0xf0
+  __DATA_CONST.__const: 0xd8
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x430
+  __DATA_CONST.__objc_selrefs: 0x460
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x180
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x3e0
-  __AUTH_CONST.__objc_const: 0xaf8
+  __AUTH_CONST.__cfstring: 0x420
+  __AUTH_CONST.__objc_const: 0xb88
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x8c
-  __DATA.__data: 0x130
-  __DATA.__bss: 0x200
+  __DATA.__objc_ivar: 0x98
+  __DATA.__data: 0x120
+  __DATA.__bss: 0x100
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__bss: 0x10
+  __DATA_DIRTY.__data: 0x10
+  __DATA_DIRTY.__bss: 0x110
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 1E742A8B-8507-3380-883E-DB650F6908DD
-  Functions: 108
-  Symbols:   510
-  CStrings:  341
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  UUID: DFAEEA84-4CE8-3C7E-91EE-5DE4CDB815DE
+  Functions: 114
+  Symbols:   521
+  CStrings:  358
 
Symbols:
+ -[PFCStoredPhoto creationDate]
+ -[PFCStoredPhoto setCreationDate:]
+ -[PFCStoredPhoto setSubtitle:]
+ -[PFCStoredPhoto setTitle:]
+ -[PFCStoredPhoto subtitle]
+ -[PFCStoredPhoto title]
+ _OBJC_IVAR_$_PFCStoredPhoto._creationDate
+ _OBJC_IVAR_$_PFCStoredPhoto._subtitle
+ _OBJC_IVAR_$_PFCStoredPhoto._title
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_PhotosFaceCore
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_PhotosFaceCore
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_PhotosFaceCore
+ _kPFCDailyUpdateNotification
+ _objc_msgSend$setCreationDate:
+ _objc_msgSend$setSubtitle:
+ _objc_msgSend$setTitle:
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_PhotosFaceCore
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_PhotosFaceCore
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_PhotosFaceCore
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_PhotosFaceCore
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_PhotosFaceCore
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_PhotosFaceCore
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_PhotosFaceCore
CStrings:
+ "T@\"NSDate\",C,N,V_creationDate"
+ "T@\"NSString\",C,N,V_subtitle"
+ "T@\"NSString\",C,N,V_title"
+ "_creationDate"
+ "_subtitle"
+ "_title"
+ "com.apple.photosface.notification.daily"
+ "setCreationDate:"
+ "setSubtitle:"
+ "setTitle:"
+ "subtitle"
+ "title"

```
