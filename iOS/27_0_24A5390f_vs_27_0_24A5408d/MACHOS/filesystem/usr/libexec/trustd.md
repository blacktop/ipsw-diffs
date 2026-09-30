## trustd

> `/usr/libexec/trustd`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
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
-  __TEXT.__text: 0x58e00
-  __TEXT.__auth_stubs: 0x2380
-  __TEXT.__objc_stubs: 0x32a0
-  __TEXT.__objc_methlist: 0xdf4
-  __TEXT.__const: 0xbd90
+62460.2.1.0.0
+  __TEXT.__text: 0x59b58
+  __TEXT.__auth_stubs: 0x23d0
+  __TEXT.__objc_stubs: 0x3360
+  __TEXT.__objc_methlist: 0xe14
+  __TEXT.__const: 0xde40
   __TEXT.__dlopen_cstrs: 0x54
   __TEXT.__objc_classname: 0x1b4
-  __TEXT.__objc_methname: 0x2f08
-  __TEXT.__objc_methtype: 0xc5d
+  __TEXT.__objc_methname: 0x2fbe
+  __TEXT.__objc_methtype: 0xc6b
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x17
   __TEXT.__swift5_reflstr: 0x4
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0xab8
-  __TEXT.__cstring: 0x5fa4
-  __TEXT.__oslogstring: 0x5b4b
-  __TEXT.__unwind_info: 0xff8
-  __DATA_CONST.__const: 0x3da0
-  __DATA_CONST.__cfstring: 0x5b80
+  __TEXT.__gcc_except_tab: 0xae0
+  __TEXT.__cstring: 0x60c3
+  __TEXT.__oslogstring: 0x5d96
+  __TEXT.__unwind_info: 0x1018
+  __DATA_CONST.__const: 0x3dc8
+  __DATA_CONST.__cfstring: 0x5d40
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_arraydata: 0x100
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x190
-  __DATA_CONST.__auth_got: 0x11d0
-  __DATA_CONST.__got: 0x918
+  __DATA_CONST.__auth_got: 0x11f8
+  __DATA_CONST.__got: 0x930
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x1750
-  __DATA.__objc_selrefs: 0xe28
+  __DATA.__objc_selrefs: 0xe58
   __DATA.__objc_ivar: 0xd0
   __DATA.__objc_data: 0x5b8
   __DATA.__data: 0x3f8

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
+  - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 1197
-  Symbols:   881
-  CStrings:  2179
+  Functions: 1202
+  Symbols:   889
+  CStrings:  2210
 
Symbols:
+ _CFUUIDCreate
+ _CFUUIDCreateString
+ _SecGetBestEffortTime
+ _access
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
+ "TrustStore.sqlite3-journal"
+ "TrustStore.sqlite3-shm"
+ "TrustStore.sqlite3-wal"
+ "[]"
+ "[refTime] eval freshnessTime=%.0f sysTime=%.0f delta=%.0fs verifyTime=%.0f"
+ "arrayByAddingObjectsFromArray:"
+ "builder %p, eval %@, cert %ld: OCSP status revoked=%@ definitive=%@ fetchFailed=%d timedOut=%d"
+ "builder %p, eval %@, cert %ld: evaluating OCSP signer chain in child builder"
+ "builder %p, eval %@, cert %ld: failed to download ocsp response from %@, timeout=%d, error %@"
+ "builder %p, eval %@, cert %ld: response from %@ was not a valid OCSP response (treating as fetch failure)"
+ "builder %p, evaluationID %@, completed trust evaluation"
+ "builder %p, evaluationID %@, starting trust evaluation (attribution %llu)"
+ "cannot write %s: %s"
+ "characterSetWithCharactersInString:"
+ "failed to stat %s: %s"
+ "port"
+ "protocolClasses"
+ "recordSSRFShadowBuckets:forContext:"
+ "setProtocolClasses:"
+ "stringByTrimmingCharactersInSet:"
+ "timeIntervalSinceReferenceDate"
+ "trustRefTime"
+ "v28@0:8I16@20"
+ "wrong owner for %s"
- "Failed to download ocsp response %@, with error %@"
- "date"
- "timeIntervalSinceNow"
```
