## VisualLogger

> `/System/Library/PrivateFrameworks/VisualLogger.framework/VisualLogger`

```diff

-8.25.12.16.5
-  __TEXT.__text: 0x706444
-  __TEXT.__auth_stubs: 0x1be0
-  __TEXT.__const: 0x67350
-  __TEXT.__gcc_except_tab: 0x60198
-  __TEXT.__cstring: 0x16324
+9.26.5.12.5
+  __TEXT.__text: 0x707330
+  __TEXT.__const: 0x67530
+  __TEXT.__gcc_except_tab: 0x659e4
+  __TEXT.__cstring: 0x1674b
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x1b5c0
+  __TEXT.__unwind_info: 0x1c300
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_methname: 0x23
-  __TEXT.__objc_stubs: 0x60
-  __DATA_CONST.__got: 0x340
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
   __DATA_CONST.__const: 0x1458
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__weak_got: 0x28
   __DATA_CONST.__objc_selrefs: 0x18
-  __AUTH_CONST.__auth_got: 0xe00
-  __AUTH_CONST.__const: 0x31ad0
+  __DATA_CONST.__got: 0x310
+  __AUTH_CONST.__const: 0x32750
   __AUTH_CONST.__cfstring: 0x2a0
-  __DATA.__data: 0x21f0
+  __AUTH_CONST.__weak_auth_got: 0x40
+  __AUTH_CONST.__auth_got: 0xe00
+  __DATA.__data: 0x21f8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x28b0
+  __DATA.__bss: 0x27e0
   __DATA.__common: 0x298
   __DATA_DIRTY.__data: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4D83238B-6CFF-3DCC-A0D5-7F6F9A09DBD3
-  Functions: 16784
-  Symbols:   1142
-  CStrings:  2219
+  UUID: 28EB3D32-B98E-3827-AF45-C9FCB5B9C73E
+  Functions: 16951
+  Symbols:   1149
+  CStrings:  2226
 
Symbols:
+ _CFDictionaryCreateMutableCopy
+ __ZNSt3__121recursive_timed_mutex4lockEv
+ __ZNSt3__121recursive_timed_mutex6unlockEv
+ __ZNSt3__121recursive_timed_mutexC1Ev
+ __ZNSt3__121recursive_timed_mutexD1Ev
+ __ZdaPvSt19__type_descriptor_t
+ __ZnamSt19__type_descriptor_t
+ _dispatch_time
+ _kCFErrorLocalizedFailureReasonKey
+ _kCFErrorUnderlyingErrorKey
+ _objc_claimAutoreleasedReturnValue
- __ZTISt12bad_any_cast
- __ZTVSt12bad_any_cast
- _kCFErrorLocalizedDescriptionKey
- _objc_retainAutoreleasedReturnValue
CStrings:
+ " : %.*s"
+ " but no specialization is available. "
+ " which is not in the provided type list "
+ "%s: %s:%d"
+ "(mesh.colors.empty() || mesh.colors.size() == mesh.vertices.size())"
+ "-inf"
+ ". The network connection may be stalled or the server stopped reading. Restart the VisualLogger server and reconnect the client to recover."
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCV3D_VisualLogger/library/Kit/Foundation/src/NumberRef.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCV3D_VisualLogger/library/Kit/IOSurface/src/IOSurfaceRef_maybe_mno_unaligned_access.cpp"
+ "An error occurred while loading the image"
+ "Failed to convert bundle URL to string"
+ "ForType called with ArithmeticType::"
+ "HasAppleNeuralEngine"
+ "Include <Kit/Common/ArithmeticType_Half.h> to support half type."
+ "Network send did not complete within "
+ "circular_queue"
+ "circular_queue_"
+ "cv3d.cf"
+ "cv3d.function"
+ "f16"
+ "idx < p_->GetCachedBaseAddresses().size()"
+ "multiple error causes"
+ "network send timed out (connection may be stalled)"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = (lambda at /Library/Caches/com.apple.xbs/F5110103-ECCF-43ED-BCAC-46AB1B758148/TemporaryDirectory.d07Xka/Sources/AppleCV3D_VisualLogger/library/VL/VisualLogger/VisualLogger/src/VZServer.cpp:354:37)]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::con::NumbersT<cv3d::kit::memory::Mutability::Const, cv3d::kit::memory::Ownership::Shared>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::memory::Mutability::Const]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::memory::Ownership::Shared]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::memory::Protection::Unprotected]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::con::NumbersT<cv3d::kit::memory::Mutability::Const, cv3d::kit::memory::Ownership::Shared>>]"
- " : "
- " as array of type with size "
- " bytes"
- " format."
- " option"
- " | "
- "&"
- "(mesh.colors.size() == 0 || mesh.colors.size() == mesh.vertices.size())"
- "*"
- "+N9mZUAHooNvMiQnjeTJ8g"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleCV3D_VisualLogger/library/Kit/IOSurface/src/IOSurfaceRef.cpp"
- "0 "
- "An error occured while loading the image"
- "Cannot reinterpret memory region of byte size "
- "UTF8String"
- "] "
- "idx < p_->GetCachedBaseAddress().size()"
- "processInfo"
- "processName"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = (lambda at /Library/Caches/com.apple.xbs/A5A71F98-F36B-4964-8EA6-BBD17D7904DD/TemporaryDirectory.0MNCKk/Sources/AppleCV3D_VisualLogger/library/VL/VisualLogger/VisualLogger/src/VZServer.cpp:354:37)]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::con::Numbers]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::ValueData<cv3d::kit::con::Numbers>]"

```
