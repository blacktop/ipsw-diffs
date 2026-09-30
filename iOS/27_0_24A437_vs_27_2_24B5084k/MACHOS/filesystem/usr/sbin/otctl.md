## otctl

> `/usr/sbin/otctl`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-62460.2.3.0.0
-  __TEXT.__text: 0x18698
-  __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_stubs: 0x2620
+62460.40.49.502.1
+  __TEXT.__text: 0x183b4
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_stubs: 0x2640
   __TEXT.__objc_methlist: 0xd6c
-  __TEXT.__const: 0xa0
+  __TEXT.__const: 0xa8
   __TEXT.__gcc_except_tab: 0x784
-  __TEXT.__objc_methname: 0x3d8e
-  __TEXT.__cstring: 0x39f9
+  __TEXT.__objc_methname: 0x3d68
+  __TEXT.__cstring: 0x3988
   __TEXT.__objc_classname: 0xad
   __TEXT.__objc_methtype: 0x4fa
   __TEXT.__oslogstring: 0xa1f
-  __TEXT.__unwind_info: 0x538
+  __TEXT.__unwind_info: 0x540
   __DATA_CONST.__const: 0x4b8
-  __DATA_CONST.__cfstring: 0x11c0
+  __DATA_CONST.__cfstring: 0x1220
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA_CONST.__auth_got: 0x2f8
+  __DATA_CONST.__auth_got: 0x2f0
   __DATA_CONST.__got: 0x190
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0xff0
-  __DATA.__objc_selrefs: 0xe88
+  __DATA.__objc_selrefs: 0xe90
   __DATA.__objc_ivar: 0xd8
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x128

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 341
-  Symbols:   156
-  CStrings:  1216
+  Functions: 343
+  Symbols:   155
+  CStrings:  1215
 
Symbols:
+ _OBJC_CLASS_$_MetricSessionInfo
- _kSecurityRTCEventCategoryAccountDataAccessRecovery
- _objc_retain_x28
CStrings:
+ "  %s%lu pairs\n"
+ "Allowed MID/Stable IDs:           "
+ "Evicted Removals:                 "
+ "Unknown Reason Removals:          "
+ "User-Initiated Removals:          "
+ "allowed_mid_stable_trusted_device_ids"
+ "initWithSession:eventName:"
+ "sessionInfoWithAltDSID:flowID:deviceSessionID:"
+ "v104@?0@\"NSSet\"8@\"NSSet\"16@\"NSSet\"24@\"NSSet\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSNumber\"64@\"NSString\"72@\"OTMetricsSessionData\"80q88@\"NSError\"96"
- "    - %s\n"
- "  Evicted Removals:                 %lu devices\n"
- "  Machine IDs:                      %lu devices\n"
- "  Stable Trusted Device IDs:        %lu pairs\n"
- "  Unknown Reason Removals:          %lu devices\n"
- "  User-Initiated Removals:          %lu devices\n"
- "initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:canSendMetrics:category:"
- "machine_ids"
- "mid_stable_trusted_device_ids"
- "v112@?0@\"NSSet\"8@\"NSSet\"16@\"NSSet\"24@\"NSSet\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSNumber\"64@\"NSString\"72@\"OTMetricsSessionData\"80@\"NSSet\"88q96@\"NSError\"104"
```
