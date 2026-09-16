## com.apple.health.records.legacy-ingestion

> `/System/Library/PrivateFrameworks/HealthRecordServices.framework/XPCServices/com.apple.health.records.legacy-ingestion.xpc/com.apple.health.records.legacy-ingestion`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-7027.0.72.2.7
-  __TEXT.__text: 0xb048
+7027.1.36.2.7
+  __TEXT.__text: 0xb4ec
   __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_stubs: 0x22e0
-  __TEXT.__objc_methlist: 0xe94
-  __TEXT.__objc_methname: 0x2a4e
-  __TEXT.__cstring: 0xd1d
+  __TEXT.__objc_stubs: 0x23c0
+  __TEXT.__objc_methlist: 0xeac
+  __TEXT.__objc_methname: 0x2b60
+  __TEXT.__cstring: 0xd44
   __TEXT.__objc_classname: 0x2e4
   __TEXT.__objc_methtype: 0x83c
   __TEXT.__const: 0x38
-  __TEXT.__oslogstring: 0x5d8
-  __TEXT.__unwind_info: 0x498
-  __DATA_CONST.__const: 0x388
+  __TEXT.__oslogstring: 0x676
+  __TEXT.__unwind_info: 0x4a8
+  __DATA_CONST.__const: 0x3b0
   __DATA_CONST.__cfstring: 0xe60
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0x280
-  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__got: 0x1e8
   __DATA.__objc_const: 0x1b20
-  __DATA.__objc_selrefs: 0xa48
+  __DATA.__objc_selrefs: 0xa80
   __DATA.__objc_ivar: 0xe4
   __DATA.__objc_data: 0x6e0
   __DATA.__data: 0x240

   - /System/Library/PrivateFrameworks/HealthRecordServices.framework/HealthRecordServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 327
-  Symbols:   195
-  CStrings:  692
+  Functions: 330
+  Symbols:   197
+  CStrings:  702
 
Symbols:
+ _OBJC_CLASS_$_HDHealthRecordsIngestionServiceClient
+ _OBJC_CLASS_$__HKBehavior
CStrings:
+ "%{public}@ completed healthrecordsd refresh for account %{public}@ with %{public}@"
+ "%{public}@ refreshing credential via healthrecordsd for account %{public}@"
+ "_refreshBadCredentialViaHealthRecordsDaemon:completion:"
+ "_refreshCredentialViaRefreshTokenTask:completion:"
+ "features"
+ "initWithAccessToken:refreshToken:patientID:expiration:scope:"
+ "markCredentialAsBadAndRefresh:forAccountWithIdentifier:completion:"
+ "newTokenRefresh"
+ "sharedBehavior"
+ "v24@?0@\"HKFHIRCredential\"8@\"NSError\"16"
```
