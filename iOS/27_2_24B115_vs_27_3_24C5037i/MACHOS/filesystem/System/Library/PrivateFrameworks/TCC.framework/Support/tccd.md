## tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-921.0.2.0.0
-  __TEXT.__text: 0x8fd4c
+925.0.4.0.0
+  __TEXT.__text: 0x902c0
   __TEXT.__auth_stubs: 0x1650
-  __TEXT.__objc_stubs: 0xbd00
-  __TEXT.__objc_methlist: 0x57d4
-  __TEXT.__cstring: 0x13838
+  __TEXT.__objc_stubs: 0xbd40
+  __TEXT.__objc_methlist: 0x57ec
+  __TEXT.__cstring: 0x1390b
   __TEXT.__const: 0x6f8
-  __TEXT.__gcc_except_tab: 0x344c
-  __TEXT.__objc_methname: 0x13c02
-  __TEXT.__oslogstring: 0x1135e
+  __TEXT.__gcc_except_tab: 0x3484
+  __TEXT.__objc_methname: 0x13c89
+  __TEXT.__oslogstring: 0x113a2
   __TEXT.__objc_classname: 0x6f2
-  __TEXT.__objc_methtype: 0x2383
+  __TEXT.__objc_methtype: 0x2387
   __TEXT.__dlopen_cstrs: 0xd9
   __TEXT.__unwind_info: 0x25f8
   __DATA_CONST.__const: 0x2a00
-  __DATA_CONST.__cfstring: 0x8f00
+  __DATA_CONST.__cfstring: 0x8f40
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1a0
-  __DATA_CONST.__objc_intobj: 0x678
+  __DATA_CONST.__objc_intobj: 0x690
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__objc_arraydata: 0x1630
+  __DATA_CONST.__objc_arraydata: 0x1640
   __DATA_CONST.__objc_arrayobj: 0xf0
-  __DATA_CONST.__objc_dictobj: 0xf28
+  __DATA_CONST.__objc_dictobj: 0xf50
   __DATA_CONST.__auth_got: 0xb38
-  __DATA_CONST.__got: 0x4e8
+  __DATA_CONST.__got: 0x4f8
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA.__objc_const: 0xa848
-  __DATA.__objc_selrefs: 0x38b0
-  __DATA.__objc_ivar: 0x784
+  __DATA.__objc_const: 0xa878
+  __DATA.__objc_selrefs: 0x38c0
+  __DATA.__objc_ivar: 0x788
   __DATA.__objc_data: 0x13b0
   __DATA.__data: 0x740
   __DATA.__common: 0x30

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3138
-  Symbols:   512
-  CStrings:  6102
+  Functions: 3141
+  Symbols:   513
+  CStrings:  6110
 
Symbols:
+ ___kCFBooleanFalse
CStrings:
+ "%s removed service-policy FDA/EndpointSecurityClient denial records"
+ "-[TCCDPlatform sendAnalyticsForAction:service:subjectIdentity:indirectObjectIdentity:authValue:includeV1AuthValue:v1AuthValue:desiredAuth:domainReason:promptType:fullSheetPrompt:includesLearnMoreLink:oneTimeReprompted:reprompted:macBuddyStatus:]_block_invoke"
+ "DELETE FROM access WHERE service IN ('kTCCServiceSystemPolicyAllFiles', 'kTCCServiceEndpointSecurityClient') AND auth_reason = %d AND auth_value = %d"
+ "FDA_WARNING"
+ "TB,N,V_doNotStoreDefaultDenyAccess"
+ "_doNotStoreDefaultDenyAccess"
+ "doNotStoreDefaultDenyAccess"
+ "kTCCServiceSystemPolicyPrivateFolders"
+ "sendAnalyticsForAction:service:subjectIdentity:indirectObjectIdentity:authValue:includeV1AuthValue:v1AuthValue:desiredAuth:domainReason:promptType:fullSheetPrompt:includesLearnMoreLink:oneTimeReprompted:reprompted:macBuddyStatus:"
+ "setDoNotStoreDefaultDenyAccess:"
+ "v116@0:8q16@24@32@40Q48B56Q60Q68@76q84B92B96B100B104q108"
- "-[TCCDPlatform sendAnalyticsForAction:service:subjectIdentity:indirectObjectIdentity:authValue:includeV1AuthValue:v1AuthValue:desiredAuth:domainReason:promptType:fullSheetPrompt:includesLearnMoreLink:oneTimeReprompted:macBuddyStatus:]_block_invoke"
- "sendAnalyticsForAction:service:subjectIdentity:indirectObjectIdentity:authValue:includeV1AuthValue:v1AuthValue:desiredAuth:domainReason:promptType:fullSheetPrompt:includesLearnMoreLink:oneTimeReprompted:macBuddyStatus:"
- "v112@0:8q16@24@32@40Q48B56Q60Q68@76q84B92B96B100q104"
```
