## ContinuityCaptureAgent

> `/usr/libexec/ContinuityCaptureAgent`

```diff

-665.120.8.0.0
-  __TEXT.__text: 0x280
-  __TEXT.__auth_stubs: 0x110
-  __TEXT.__objc_stubs: 0xa0
-  __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x168
-  __TEXT.__oslogstring: 0x84
-  __TEXT.__objc_methname: 0x65
+748.0.0.122.2
+  __TEXT.__text: 0x384
+  __TEXT.__auth_stubs: 0x120
+  __TEXT.__objc_stubs: 0x20
+  __TEXT.__const: 0x10
+  __TEXT.__cstring: 0x12c
+  __TEXT.__oslogstring: 0xf4
+  __TEXT.__objc_methname: 0x19
   __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__auth_got: 0x90
-  __DATA_CONST.__got: 0x18
-  __DATA_CONST.__cfstring: 0xa0
+  __DATA_CONST.__const: 0x60
+  __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x28
-  __DATA.__bss: 0x8
+  __DATA_CONST.__auth_got: 0x98
+  __DATA_CONST.__got: 0x18
+  __DATA.__objc_selrefs: 0x10
+  - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore
+  - /System/Library/PrivateFrameworks/CMContinuityCaptureHost.framework/CMContinuityCaptureHost
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 046D8A04-2F2E-32F6-9C42-BA2D6A0E70BC
-  Functions: 2
-  Symbols:   24
-  CStrings:  23
+  UUID: C311B137-2262-39C1-9615-57DE1996B603
+  Functions: 3
+  Symbols:   26
+  CStrings:  20
 
Symbols:
+ _CMContinuityCaptureLog
+ __NSConcreteGlobalBlock
+ __xpc_event_key_name
+ __xpc_type_dictionary
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _xpc_dictionary_create_reply
+ _xpc_dictionary_get_bool
+ _xpc_dictionary_get_string
+ _xpc_dictionary_send_reply
+ _xpc_get_type
+ _xpc_set_event_stream_handler
- _CFRunLoopRun
- _FigGetCFPreferenceBooleanWithDefault
- _OBJC_CLASS_$_CMContinuityCaptureProvider
- _OBJC_CLASS_$_NSFileManager
- _objc_alloc
- _objc_release_x8
- _objc_retainAutoreleasedReturnValue
- _objc_unsafeClaimAutoreleasedReturnValue
- _xpc_dictionary_create
- _xpc_dictionary_set_string
CStrings:
+ "ContinuityCaptureAgent stream event %s"
+ "Received launch event from CMIO %@"
+ "Received launch event from rapport %@"
+ "com.apple.cmio.ContinuityCaptureAgent.discovery"
+ "com.apple.rapport.matching"
+ "ignoreSIGTERM"
+ "replyRequired"
+ "v16@?0@\"NSObject<OS_xpc_object>\"8"
- "CMIOExtensionBundleIdentifier"
- "activate"
- "com.apple.cameracapture"
- "com.apple.cmio.ContinuityCaptureAgent"
- "com.apple.continuitycapture.hostLocalServer"
- "containerURLForSecurityApplicationGroupIdentifier:"
- "defaultManager"
- "group.com.apple.portrait.BackgroundReplacement"
- "initWithQueue:"

```
