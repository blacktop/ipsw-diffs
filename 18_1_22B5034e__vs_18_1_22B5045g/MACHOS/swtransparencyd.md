## swtransparencyd

> `/usr/libexec/swtransparencyd`

```diff

-1218.40.23.0.1
-  __TEXT.__text: 0xf3358
-  __TEXT.__auth_stubs: 0x2480
+1218.40.31.0.0
+  __TEXT.__text: 0xf5854
+  __TEXT.__auth_stubs: 0x2490
   __TEXT.__objc_stubs: 0x5f20
   __TEXT.__objc_methlist: 0x6cf8
-  __TEXT.__const: 0x47e0
-  __TEXT.__cstring: 0x5b18
-  __TEXT.__oslogstring: 0x321d
+  __TEXT.__const: 0x4880
+  __TEXT.__cstring: 0x5b98
+  __TEXT.__oslogstring: 0x331d
   __TEXT.__objc_classname: 0x1432
-  __TEXT.__objc_methname: 0x7763
+  __TEXT.__objc_methname: 0x7774
   __TEXT.__objc_methtype: 0x201a
   __TEXT.__gcc_except_tab: 0x540
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__swift5_typeref: 0x1387
-  __TEXT.__swift5_capture: 0x778
-  __TEXT.__swift5_fieldmd: 0x18d4
-  __TEXT.__constg_swiftt: 0x1954
-  __TEXT.__swift5_reflstr: 0x10ef
+  __TEXT.__swift5_typeref: 0x13b5
+  __TEXT.__swift5_capture: 0x78c
+  __TEXT.__swift5_fieldmd: 0x1934
+  __TEXT.__constg_swiftt: 0x1998
+  __TEXT.__swift5_reflstr: 0x1165
   __TEXT.__swift5_protos: 0x30
-  __TEXT.__swift5_proto: 0x360
+  __TEXT.__swift5_proto: 0x364
   __TEXT.__swift5_types: 0x1ac
   __TEXT.__swift5_assocty: 0x1c8
-  __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_mpenum: 0x60
+  __TEXT.__swift5_builtin: 0x104
+  __TEXT.__swift5_mpenum: 0x74
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x4970
-  __TEXT.__eh_frame: 0x616c
-  __DATA_CONST.__auth_got: 0x1250
+  __TEXT.__unwind_info: 0x49e0
+  __TEXT.__eh_frame: 0x627c
+  __DATA_CONST.__auth_got: 0x1258
   __DATA_CONST.__got: 0x648
-  __DATA_CONST.__auth_ptr: 0x530
-  __DATA_CONST.__const: 0x5d18
+  __DATA_CONST.__auth_ptr: 0x5f0
+  __DATA_CONST.__const: 0x5c58
   __DATA_CONST.__cfstring: 0x3100
   __DATA_CONST.__objc_classlist: 0x658
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x308
-  __DATA.__objc_const: 0xfd20
-  __DATA.__objc_selrefs: 0x2160
+  __DATA.__objc_const: 0xfd80
+  __DATA.__objc_selrefs: 0x2168
   __DATA.__objc_ivar: 0x478
   __DATA.__objc_data: 0x3c70
-  __DATA.__data: 0x5080
-  __DATA.__bss: 0x7018
-  __DATA.__common: 0x2d8
+  __DATA.__data: 0x5190
+  __DATA.__bss: 0x70a8
+  __DATA.__common: 0x2e8
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6046
-  Symbols:   905
-  CStrings:  3176
+  Functions: 6083
+  Symbols:   906
+  CStrings:  3181
 
Symbols:
+ _swift_getTupleTypeLayout2
CStrings:
+ "Public key response for %!{(MISSING)public}s older than refresh period"
+ "pendingFetch"
+ "TLT STH keys for %!{(MISSING)public}s need refresh"
+ "failed to configure %!{(MISSING)public}s from disk public key key bag: %!@(MISSING)"
+ "com.apple.SWTKeyBagFetcherError "
+ "Detected new ATL epoch: %!{(MISSING)public}s - %!{(MISSING)public}lld"
+ "Detected a PAT reset from %!{(MISSING)public}llu to %!{(MISSING)public}llu"
+ "Failed to verify signature for %!{(MISSING)public}s: %!@(MISSING)"
+ "Detected new TLT epoch: %!{(MISSING)public}s"
+ "Opening existing swt database with schema version 1. Dropping table and replacing with schema version %!{(MISSING)public}ld."
+ "Detected new PAT epoch: %!{(MISSING)public}s"
+ "Opening existing swt database with schema version %!{(MISSING)public}ld"
+ "Verified %!{(MISSING)public}s consistency proof chunk %!l(MISSING)d"
+ "Creating new swt database with schema version %!{(MISSING)public}ld."
+ "Failed to verify inclusion proof for %!{(MISSING)public}s"
+ "have key bag for %!{(MISSING)public}s, but triggering refresh"
+ "Found %!{(MISSING)public}s AT split view from before CFU delay for %!{(MISSING)public}lld epoch"
+ "Detected a TLT reset from %!{(MISSING)public}llu to %!{(MISSING)public}llu"
+ "swtransparencyd started at: %!{(MISSING)public}lu kt: %!{(MISSING)public}lu"
+ "Using prod key bag for %!{(MISSING)public}s"
+ "Failed to verify consistency for %!{(MISSING)public}s"
+ "HTTP fetch failed with: "
+ "No key bag for %!{(MISSING)public}s"
+ "Rejecting connection from unauthorized client %!{(MISSING)public}s because it's missing the com.apple.transparency.privateCloudCompute entitlement"
+ "userRequest"
+ "underlyingErrors"
+ "Unable to find trusted key for SPKI hash: %!{(MISSING)public}@"
+ "Using carry key bag for %!{(MISSING)public}s"
+ "Found %!{(MISSING)public}s PAT split view from before CFU delay for %!{(MISSING)public}llu epoch"
+ "Accepting new connection from %!{(MISSING)public}s"
+ "postCFU: %!{(MISSING)public}s"
+ "App STH keys for %!{(MISSING)public}s need refresh"
+ "Failed to verify signature for %!{(MISSING)public}s"
- "Opening existing swt database with schema version %!l(MISSING)d"
- "Public key response for %!s(MISSING) older than refresh period"
- "Found %!s(MISSING) PAT split view from before CFU delay for %!l(MISSING)lu epoch"
- "failed to configure %!s(MISSING) from disk public key key bag: %!@(MISSING)"
- "triggerPublicKeyBagFetch"
- "Using carry key bag for %!s(MISSING)"
- "Failed to verify signature for %!s(MISSING): %!@(MISSING)"
- "TLT STH keys for %!s(MISSING) need refresh"
- "Verified %!s(MISSING) consistency proof chunk %!l(MISSING)d"
- "Using prod key bag for %!s(MISSING)"
- "Failed to verify signature for %!s(MISSING)"
- "Detected new PAT epoch: %!s(MISSING)"
- "Detected a TLT reset from %!l(MISSING)lu to %!l(MISSING)lu"
- "Found %!s(MISSING) AT split view from before CFU delay for %!l(MISSING)ld epoch"
- "App STH keys for %!s(MISSING) need refresh"
- "Failed to verify consistency for %!s(MISSING)"
- "have key bag for %!s(MISSING), but triggering refresh"
- "Rejecting connection from unauthorized client %!s(MISSING) because it's missing the com.apple.transparency.privateCloudCompute entitlement"
- "Accepting new connection from %!s(MISSING)"
- "Detected new TLT epoch: %!s(MISSING)"
- "Detected a PAT reset from %!l(MISSING)lu to %!l(MISSING)lu"
- "Opening existing swt database with schema version 1. Dropping table and replacing with schema version %!l(MISSING)d."
- "postCFU: %!s(MISSING)"
- "swtransparencyd started at: %!l(MISSING)u kt: %!l(MISSING)u"
- "No key bag for %!s(MISSING)"
- "Detected new ATL epoch: %!s(MISSING) - %!l(MISSING)ld"
- "Creating new swt database with schema version %!l(MISSING)d."

```
