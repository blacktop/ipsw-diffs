## CampoRemoteService

> `/System/Library/PrivateFrameworks/CampoUIServices.framework/Versions/Current/XPCServices/CampoRemoteService.xpc/Contents/MacOS/CampoRemoteService`

```diff

-  __TEXT.__text: 0x2d824
-  __TEXT.__auth_stubs: 0x1910
-  __TEXT.__objc_stubs: 0x5e0
-  __TEXT.__objc_methlist: 0x364
-  __TEXT.__const: 0x2024
-  __TEXT.__constg_swiftt: 0xbc8
-  __TEXT.__swift5_typeref: 0x1d7c
+  __TEXT.__text: 0x2f07c
+  __TEXT.__auth_stubs: 0x19a0
+  __TEXT.__objc_stubs: 0x600
+  __TEXT.__objc_methlist: 0x3b4
+  __TEXT.__const: 0x20d4
+  __TEXT.__constg_swiftt: 0xbe0
+  __TEXT.__swift5_typeref: 0x1ea4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__objc_classname: 0x1f2
-  __TEXT.__objc_methname: 0x88c
-  __TEXT.__objc_methtype: 0x1fd
-  __TEXT.__swift5_reflstr: 0x6f3
-  __TEXT.__swift5_fieldmd: 0x890
+  __TEXT.__objc_classname: 0x212
+  __TEXT.__objc_methname: 0x9e2
+  __TEXT.__objc_methtype: 0x24d
+  __TEXT.__swift5_reflstr: 0x753
+  __TEXT.__swift5_fieldmd: 0x90c
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__cstring: 0x78e
-  __TEXT.__swift5_capture: 0x7e8
-  __TEXT.__oslogstring: 0x621
+  __TEXT.__cstring: 0x7fe
+  __TEXT.__swift5_capture: 0x818
+  __TEXT.__oslogstring: 0x631
   __TEXT.__swift5_proto: 0x98
-  __TEXT.__swift5_types: 0xb8
+  __TEXT.__swift5_types: 0xbc
   __TEXT.__swift_as_entry: 0x50
   __TEXT.__swift_as_ret: 0x38
   __TEXT.__swift_as_cont: 0x8c
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_assocty: 0x228
-  __TEXT.__unwind_info: 0xdc0
-  __TEXT.__eh_frame: 0xfdc
-  __DATA_CONST.__const: 0x1dd8
+  __TEXT.__swift5_assocty: 0x210
+  __TEXT.__unwind_info: 0xe10
+  __TEXT.__eh_frame: 0xfe4
+  __DATA_CONST.__const: 0x1eb0
   __DATA_CONST.__objc_classlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__auth_got: 0xc90
-  __DATA_CONST.__got: 0x518
-  __DATA_CONST.__auth_ptr: 0x608
-  __DATA.__objc_const: 0x7b8
-  __DATA.__objc_selrefs: 0x2c0
-  __DATA.__objc_data: 0x498
-  __DATA.__data: 0x13d0
-  __DATA.__bss: 0x14e0
-  __DATA.__common: 0x218
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__auth_got: 0xcd8
+  __DATA_CONST.__got: 0x520
+  __DATA_CONST.__auth_ptr: 0x620
+  __DATA.__objc_const: 0x840
+  __DATA.__objc_selrefs: 0x2e0
+  __DATA.__objc_data: 0x4a0
+  __DATA.__data: 0x1590
+  __DATA.__bss: 0x14c0
+  __DATA.__common: 0x230
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SwiftUI.framework/Versions/A/SwiftUI
   - /System/Library/PrivateFrameworks/AssistantUICore.framework/Versions/A/AssistantUICore
   - /System/Library/PrivateFrameworks/CampoServices.framework/Versions/A/CampoServices
   - /System/Library/PrivateFrameworks/CampoUIInternal.framework/Versions/A/CampoUIInternal
   - /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1497
-  Symbols:   173
-  CStrings:  231
+  Functions: 1524
+  Symbols:   178
+  CStrings:  246
 
Sections:
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__objc_classlist : content changed
Symbols:
+ _SecTaskCopySigningIdentifier
+ _SecTaskCreateWithAuditToken
+ _audit_token_to_pid
+ _audit_token_to_pidversion
+ _kCFAllocatorDefault
CStrings:
+ "@24@0:8@\"NSCoder\"16"
+ "NSCampoLightweightUIInitialModeKey"
+ "NSCoding"
+ "NSSecureCoding"
+ "TB,R"
+ "_onTextChange"
+ "com.apple.AgentCanvasKit"
+ "encodeWithCoder:"
+ "hostAppAuditToken"
+ "remoteWarmUp"
+ "sourceWindowIdentifier"
+ "supportsSecureCoding"
+ "v24@0:8@\"NSCoder\"16"

```
