## com.apple.MobileAsset.DownloadService.Builtin

> `/System/Library/PrivateFrameworks/MobileAssetDaemon.framework/XPCServices/com.apple.MobileAsset.DownloadService.Builtin.xpc/com.apple.MobileAsset.DownloadService.Builtin`

```diff

-1837.122.1.0.0
-  __TEXT.__text: 0x23a44
-  __TEXT.__auth_stubs: 0xc70
-  __TEXT.__objc_stubs: 0x4600
-  __TEXT.__objc_methlist: 0x1e3c
+2215.0.0.502.1
+  __TEXT.__text: 0x216bc
+  __TEXT.__auth_stubs: 0xd70
+  __TEXT.__objc_stubs: 0x46a0
+  __TEXT.__objc_methlist: 0x1e74
   __TEXT.__const: 0x69c
-  __TEXT.__cstring: 0x415c
-  __TEXT.__gcc_except_tab: 0x1424
-  __TEXT.__objc_methname: 0x5e4c
-  __TEXT.__oslogstring: 0x5f41
-  __TEXT.__objc_classname: 0x35e
-  __TEXT.__objc_methtype: 0x1224
+  __TEXT.__cstring: 0x43d9
+  __TEXT.__gcc_except_tab: 0x1184
+  __TEXT.__objc_methname: 0x5ea7
+  __TEXT.__oslogstring: 0x6051
+  __TEXT.__objc_classname: 0x33e
+  __TEXT.__objc_methtype: 0x1254
   __TEXT.__swift5_typeref: 0xda
   __TEXT.__constg_swiftt: 0xa0
   __TEXT.__swift5_fieldmd: 0x2c

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x880
-  __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0x648
-  __DATA_CONST.__got: 0x348
-  __DATA_CONST.__auth_ptr: 0x160
+  __TEXT.__unwind_info: 0x750
+  __TEXT.__eh_frame: 0xc4
   __DATA_CONST.__const: 0x860
-  __DATA_CONST.__cfstring: 0x2ba0
+  __DATA_CONST.__cfstring: 0x2d60
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0xc0
-  __DATA_CONST.__objc_arraydata: 0x388
-  __DATA_CONST.__objc_dictobj: 0x140
+  __DATA_CONST.__objc_arraydata: 0x458
+  __DATA_CONST.__objc_dictobj: 0x230
   __DATA_CONST.__objc_arrayobj: 0x78
+  __DATA_CONST.__auth_got: 0x6c8
+  __DATA_CONST.__got: 0x350
+  __DATA_CONST.__auth_ptr: 0x168
   __DATA.__objc_const: 0x31c0
-  __DATA.__objc_selrefs: 0x1540
+  __DATA.__objc_selrefs: 0x1560
   __DATA.__objc_ivar: 0x274
   __DATA.__objc_data: 0x5b8
   __DATA.__data: 0x698
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x520
+  __DATA.__bss: 0x548
   - /System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: CF0DAEC3-AAF1-3228-9C73-EDD4802B4AEB
-  Functions: 678
-  Symbols:   332
-  CStrings:  2308
+  UUID: 6A27C397-B6DF-3AF1-A95E-F1C5F8159818
+  Functions: 685
+  Symbols:   349
+  CStrings:  2358
 
Symbols:
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ __CFNetworkSetATSContext
+ __availability_version_check
+ _dispatch_once_f
+ _dlsym
+ _fclose
+ _fopen
+ _fread
+ _fseek
+ _ftell
+ _malloc
+ _objc_claimAutoreleasedReturnValue
+ _objc_opt_respondsToSelector
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _rewind
+ _sscanf
- _objc_retain_x26
CStrings:
+ "%d.%d.%d"
+ "/System/Library/CoreServices/SystemVersion.plist"
+ "@52@0:8@16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24@32B40^@44"
+ "AutoSet-CheckMetadata"
+ "CFDataCreateWithBytesNoCopy"
+ "CFDictionaryGetValue"
+ "CFGetTypeID"
+ "CFPropertyListCreateFromXMLData"
+ "CFPropertyListCreateWithData"
+ "CFRelease"
+ "CFStringCreateWithCStringNoCopy"
+ "CFStringGetCString"
+ "CFStringGetTypeID"
+ "NSAllowsArbitraryLoads"
+ "NSExceptionAllowsInsecureHTTPLoads"
+ "NSExceptionDomains"
+ "NSExceptionRequiresNIAPTLSPackageVersion"
+ "NSRequiresNIAPTLSPackageVersion"
+ "ProductVersion"
+ "[KnoxServerAuth] Skipping ATS trust policy for %@"
+ "[MAConfigureTrustPolicy]: Failed to setup policy"
+ "[MAConfigureTrustPolicy]: Failed to setup policy(serialization of policy dictionary failed):%{public}@"
+ "[MAConfigureTrustPolicy]: Policy setup successful"
+ "[MAConfigureTrustPolicy]: Setting up ATS policy"
+ "[MAConfigureTrustPolicy]: Setting up legacy ATS policy"
+ "[MADownloadServiceBuiltin]: Attempting to start up builtin service built Jun  1 2026 21:29:50"
+ "[Manager]: Download Request for task | TaskDescriptor:%{public}@ | IsContentCache:%{public}@ | URL:%{public}@"
+ "[Manager]: Finished obtaining extrator | TaskDescriptor:%{public}@"
+ "[Manager]: Obtaining extractor | TaskDescriptor:%{public}@"
+ "[STExtractorWrapper]: Final AppleConnect UI status: %{public}@"
+ "appldnld.apple.com"
+ "cheeserolling.apple.com"
+ "com.apple.MobileAsset.PSUSConfig.AutoAssetSetTargets"
+ "currentRequest"
+ "dataWithPropertyList:format:options:error:"
+ "kCFAllocatorNull"
+ "none"
+ "r"
+ "recommended"
+ "setATSPolicy"
+ "set_atsTrustPolicy:"
+ "updates-http.cdn-apple.com"
- "@52@0:8@16^{__SecKey=}24@32B40^@44"
- "[MADownloadServiceBuiltin]: Attempting to start up builtin service built Apr 22 2026 22:29:57"
- "[Manager]: Attempting to obtain extractor for task | TaskDescriptor:%{public}@"
- "[Manager]: Constructing download request for knox asset download | TaskDescriptor:%{public}@ | URL: %{public}@"
- "[Manager]: Successfully generated extractor for task | TaskDescriptor:%{public}@"
- "[Manager]: Using passed in download request for asset download | knoxURL:%{public}@ | DecryptionKey:%{public}@"

```
