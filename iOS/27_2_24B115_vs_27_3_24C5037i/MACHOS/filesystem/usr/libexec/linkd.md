## linkd

> `/usr/libexec/linkd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__objc_methtype`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_data`

```diff

-301.1.16.0.0
-  __TEXT.__text: 0xc0024
-  __TEXT.__auth_stubs: 0x2a50
+301.2.7.2.0
+  __TEXT.__text: 0xc1574
+  __TEXT.__auth_stubs: 0x2a70
   __TEXT.__objc_stubs: 0x27e0
-  __TEXT.__objc_methlist: 0xe0c
+  __TEXT.__objc_methlist: 0xdfc
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x5ddc
-  __TEXT.__constg_swiftt: 0x1d80
-  __TEXT.__swift5_typeref: 0x2e02
+  __TEXT.__const: 0x5e2c
+  __TEXT.__constg_swiftt: 0x1d78
+  __TEXT.__swift5_typeref: 0x2e12
   __TEXT.__swift5_builtin: 0x1cc
   __TEXT.__swift5_reflstr: 0x1318
   __TEXT.__swift5_fieldmd: 0x1704

   __TEXT.__swift5_proto: 0x364
   __TEXT.__swift5_types: 0x1d0
   __TEXT.__objc_classname: 0x909
-  __TEXT.__objc_methname: 0x3ffd
+  __TEXT.__objc_methname: 0x3fbd
   __TEXT.__objc_methtype: 0x188b
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__cstring: 0x1c80
-  __TEXT.__swift5_capture: 0x2f30
-  __TEXT.__swift_as_entry: 0x594
-  __TEXT.__swift_as_cont: 0x758
-  __TEXT.__oslogstring: 0x4f81
+  __TEXT.__cstring: 0x1d40
+  __TEXT.__swift5_capture: 0x2ee4
+  __TEXT.__swift_as_entry: 0x598
+  __TEXT.__swift_as_ret: 0x570
+  __TEXT.__swift_as_cont: 0x788
+  __TEXT.__oslogstring: 0x50a1
   __TEXT.__swift5_protos: 0x68
-  __TEXT.__swift_as_ret: 0x560
-  __TEXT.__unwind_info: 0x4500
-  __TEXT.__eh_frame: 0xa3b8
-  __DATA_CONST.__const: 0x9b48
+  __TEXT.__unwind_info: 0x4558
+  __TEXT.__eh_frame: 0xa4c8
+  __DATA_CONST.__const: 0x9a80
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__auth_got: 0x1530
-  __DATA_CONST.__got: 0xa90
-  __DATA_CONST.__auth_ptr: 0x1468
-  __DATA.__objc_const: 0x22a8
-  __DATA.__objc_selrefs: 0xe40
+  __DATA_CONST.__auth_got: 0x1540
+  __DATA_CONST.__got: 0xa98
+  __DATA_CONST.__auth_ptr: 0x1480
+  __DATA.__objc_const: 0x22a0
+  __DATA.__objc_selrefs: 0xe38
   __DATA.__objc_data: 0x8e8
-  __DATA.__data: 0x3c10
+  __DATA.__data: 0x3c30
   __DATA.__common: 0x320
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5615
-  Symbols:   1202
-  CStrings:  1240
+  Functions: 5612
+  Symbols:   1205
+  CStrings:  1246
 
Symbols:
+ _$s15AppIntentsIndex08MetadataC0V17bundlesWithSkillsSaySSGyKF
+ _$s15AppIntentsIndex08MetadataC0V5skill19forBundleIdentifier0E4NameSo07LNSkillD0CSgSS_SStKF
+ _$s15AppIntentsIndex08MetadataC0V6skills19forBundleIdentifierSaySo07LNSkillD0CGSS_tKF
+ _$sScG4next9isolationxSgScA_pSgYi_tYaF
+ _$sScG4next9isolationxSgScA_pSgYi_tYaFTu
+ _OBJC_CLASS_$_LNSkillMetadata
- _$s15AppIntentsIndex08MetadataC0V19setIntentEnablement16bundleIdentifier06actionI010enablementySS_SSSo08LNIntentG0CtKF
- _$s15AppIntentsIndex08MetadataC0V20getIntentEnablements16bundleIdentifierSDySSSo18LNIntentEnablementCGSS_tKF
- _OBJC_CLASS_$_LNIntentEnablement
CStrings:
+ "%s: Delivery to %s failed or timed out: %@"
+ "EntitlementAudit: %{public}s (pid %{public}d) lacks %{public}s, REJECTED for %{public}s"
+ "Ordering violation: .updated for %s after .deleted in the same batch"
+ "Unknown event type %ld — passing through uncoalesced"
+ "_fetchListenerEndpoint(forProcessInstanceIdentifier:)"
+ "_fetchProcessInstanceIdentifiers(forBundleIdentifier:)"
+ "_fetchProcessInstanceIdentifiersGroupedByBundleIdentifier()"
+ "bundlesWithSkillsWithReply:"
+ "eventType"
+ "eventWithType:bundleIdentifier:entityType:instanceIdentifiers:"
+ "instanceIdentifiers"
+ "skillForBundleIdentifier:skillName:reply:"
+ "skillsForBundleIdentifier:reply:"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"LNSkillMetadata\"@\"NSError\">32"
- "disabledWithReason:"
- "enabled"
- "persistIntentEnablementForIntent:enablement:reply:"
- "retrieveEnabledIntentsWithReply:"
- "retrievePersistedIntentEnablementsWithReply:"
- "setIntentEnabled:enabled:reply:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "v40@0:8@\"NSString\"16@\"LNIntentEnablement\"24@?<v@?@\"NSError\">32"
```
