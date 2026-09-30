## trustd

> `/usr/libexec/trustd`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-62460.0.55.0.1
-  __TEXT.__text: 0x5c448
-  __TEXT.__auth_stubs: 0x2320
-  __TEXT.__objc_stubs: 0x3300
-  __TEXT.__objc_methlist: 0xdf4
-  __TEXT.__const: 0xbc60
+62460.1.2.0.0
+  __TEXT.__text: 0x5d044
+  __TEXT.__auth_stubs: 0x2360
+  __TEXT.__objc_stubs: 0x33c0
+  __TEXT.__objc_methlist: 0xe14
+  __TEXT.__const: 0xdd20
   __TEXT.__dlopen_cstrs: 0x54
   __TEXT.__objc_classname: 0x1b4
-  __TEXT.__objc_methname: 0x2f6a
-  __TEXT.__objc_methtype: 0xc5d
+  __TEXT.__objc_methname: 0x3020
+  __TEXT.__objc_methtype: 0xc6b
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x17
   __TEXT.__swift5_reflstr: 0x4
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0xbc0
-  __TEXT.__cstring: 0x5bee
-  __TEXT.__oslogstring: 0x5c4e
-  __TEXT.__unwind_info: 0x1040
+  __TEXT.__gcc_except_tab: 0xbe0
+  __TEXT.__cstring: 0x5cc4
+  __TEXT.__oslogstring: 0x5e5c
+  __TEXT.__unwind_info: 0x1058
   __DATA_CONST.__const: 0x4308
-  __DATA_CONST.__cfstring: 0x5820
+  __DATA_CONST.__cfstring: 0x5980
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_arraydata: 0x100
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x190
-  __DATA_CONST.__auth_got: 0x11a0
-  __DATA_CONST.__got: 0x8e8
+  __DATA_CONST.__auth_got: 0x11c0
+  __DATA_CONST.__got: 0x900
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x1750
-  __DATA.__objc_selrefs: 0xe40
+  __DATA.__objc_selrefs: 0xe70
   __DATA.__objc_ivar: 0xd0
   __DATA.__objc_data: 0x5b8
   __DATA.__data: 0x428

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/Versions/A/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/Versions/A/BiomeStreams
+  - /System/Library/PrivateFrameworks/CoreTime.framework/Versions/A/CoreTime
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/Versions/A/CrashReporterSupport
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/Versions/A/MSUDataAccessor
   - /System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/MobileAsset

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 1263
-  Symbols:   869
-  CStrings:  2165
+  Functions: 1268
+  Symbols:   876
+  CStrings:  2190
 
Symbols:
+ _CFUUIDCreate
+ _CFUUIDCreateString
+ _SecGetBestEffortTime
+ _inet_pton
+ _kSecTrustInfoEvaluationIDKey
+ _kSecTrustInfoOCSPFetchFailedKey
+ _kSecTrustInfoOCSPTimedOutKey
CStrings:
+ "CAIssuerSSRFBadPort"
+ "CAIssuerSSRFLinkLocal"
+ "CAIssuerSSRFLoopback"
+ "CAIssuerSSRFOtherReserved"
+ "CAIssuerSSRFRFC1918"
+ "OCSPSSRFBadPort"
+ "OCSPSSRFLinkLocal"
+ "OCSPSSRFLoopback"
+ "OCSPSSRFOtherReserved"
+ "OCSPSSRFRFC1918"
+ "[]"
+ "[refTime] eval freshnessTime=%.0f sysTime=%.0f delta=%.0fs verifyTime=%.0f"
+ "arrayByAddingObjectsFromArray:"
+ "builder %p, eval %@, cert %ld: OCSP status revoked=%@ definitive=%@ fetchFailed=%d timedOut=%d"
+ "builder %p, eval %@, cert %ld: evaluating OCSP signer chain in child builder"
+ "builder %p, eval %@, cert %ld: failed to download ocsp response from %@, timeout=%d, error %@"
+ "builder %p, eval %@, cert %ld: response from %@ was not a valid OCSP response (treating as fetch failure)"
+ "builder %p, evaluationID %@, completed trust evaluation"
+ "builder %p, evaluationID %@, starting trust evaluation (attribution %llu)"
+ "characterSetWithCharactersInString:"
+ "port"
+ "protocolClasses"
+ "recordSSRFShadowBuckets:forContext:"
+ "setProtocolClasses:"
+ "stringByTrimmingCharactersInSet:"
+ "timeIntervalSinceReferenceDate"
+ "trustRefTime"
+ "v28@0:8I16@20"
- "Failed to download ocsp response %@, with error %@"
- "date"
- "timeIntervalSinceNow"
```
