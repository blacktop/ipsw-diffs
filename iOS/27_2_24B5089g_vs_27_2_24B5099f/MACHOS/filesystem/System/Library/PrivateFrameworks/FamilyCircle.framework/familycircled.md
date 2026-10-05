## familycircled

> `/System/Library/PrivateFrameworks/FamilyCircle.framework/familycircled`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-291.125.4.0.0
-  __TEXT.__text: 0xb1984
-  __TEXT.__auth_stubs: 0x2a60
-  __TEXT.__objc_stubs: 0x5ba0
-  __TEXT.__objc_methlist: 0x27bc
-  __TEXT.__oslogstring: 0x656d
-  __TEXT.__cstring: 0x31f2
+291.125.7.0.0
+  __TEXT.__text: 0xb1f74
+  __TEXT.__auth_stubs: 0x2a80
+  __TEXT.__objc_stubs: 0x5cc0
+  __TEXT.__objc_methlist: 0x27dc
+  __TEXT.__oslogstring: 0x672d
+  __TEXT.__cstring: 0x3232
   __TEXT.__objc_classname: 0xd3d
-  __TEXT.__const: 0x4344
-  __TEXT.__objc_methname: 0x7c9b
-  __TEXT.__objc_methtype: 0x22bc
-  __TEXT.__gcc_except_tab: 0x1f8
+  __TEXT.__const: 0x4354
+  __TEXT.__objc_methname: 0x7e6b
+  __TEXT.__objc_methtype: 0x243c
+  __TEXT.__gcc_except_tab: 0x208
   __TEXT.__dlopen_cstrs: 0x14f
-  __TEXT.__swift5_typeref: 0x1b23
-  __TEXT.__swift5_capture: 0xf9c
+  __TEXT.__swift5_typeref: 0x1b4b
+  __TEXT.__swift5_capture: 0xfa8
   __TEXT.__constg_swiftt: 0x18fc
   __TEXT.__swift5_reflstr: 0x1046
   __TEXT.__swift5_fieldmd: 0xfc8

   __TEXT.__swift_as_cont: 0x740
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__unwind_info: 0x3e70
-  __TEXT.__eh_frame: 0x8c1c
+  __TEXT.__unwind_info: 0x3e88
+  __TEXT.__eh_frame: 0x8cac
   __DATA_CONST.__const: 0x5560
   __DATA_CONST.__cfstring: 0x13a0
   __DATA_CONST.__objc_classlist: 0x278

   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x1540
-  __DATA_CONST.__got: 0x9d8
+  __DATA_CONST.__auth_got: 0x1550
+  __DATA_CONST.__got: 0x9d0
   __DATA_CONST.__auth_ptr: 0x828
-  __DATA.__objc_const: 0x8a38
-  __DATA.__objc_selrefs: 0x1be8
+  __DATA.__objc_const: 0x8a40
+  __DATA.__objc_selrefs: 0x1c30
   __DATA.__objc_ivar: 0x1b8
   __DATA.__objc_data: 0x2820
-  __DATA.__data: 0x29f8
+  __DATA.__data: 0x29d8
   __DATA.__common: 0x90
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3459
-  Symbols:   1206
-  CStrings:  2362
+  Functions: 3461
+  Symbols:   1207
+  CStrings:  2377
 
Symbols:
+ _$s10Foundation4DateV2leoiySbAC_ACtFZ
+ _$s12FamilyCircle11XPCActivityC8CriteriaV7OptionsV10wakeDeviceAGvgZ
+ _$s12FamilyCircle11XPCActivityC8PriorityO13userInitiatedyA2EmFWC
+ __FAAgeAttestationLogSystem
- _$s10Foundation4DateVSLAAMc
- _$s12FamilyCircle11XPCActivityC8PriorityO7utilityyA2EmFWC
- _$sSL2leoiySbx_xtFZTj
CStrings:
+ "Applying account restrictions through ScreenTime settings. managementSettings.isManaged=%{public}s managementSettings.hasStrictPolicy=%{bool,public}d"
+ "Applying proto account restrictions (%lu) through ScreenTime settings. managementSettings.isManaged=%{public}s managementSettings.hasStrictPolicy=%{bool,public}d"
+ "STExpressIntroductionUserObjC"
+ "Setting account restrictions through ST settings with additional headers. managementSettings.isManaged=%@ managementSettings.hasStrictPolicy=%d"
+ "Setting proto account restrictions (%lu) through ST settings. managementSettings.isManaged=%@ managementSettings.hasStrictPolicy=%d"
+ "applyDefaultRestrictionsForAccount(with:presetsRequest:additionalHeaders:managementSettings:)"
+ "applyDefaultRestrictionsForAccountWithScreenTimeCore:presetsRequest:additionalHeaders:managementSettings:completion:"
+ "applyDefaultRestrictionsForProtoAccountWithScreenTimeCore:managementSettings:completion:"
+ "applyRestrictionsForProtoAccount(_:managementSettings:screenTimeCore:)"
+ "applyRestrictionsForProtoAccount:managementSettings:screenTimeCore:completion:"
+ "familyDeviceListInformationForAltDSID:operatingSystems:replyBlock:"
+ "hasStrictPolicy"
+ "initWithQueueProvider:authenticationController:"
+ "isManaged"
+ "localUser"
+ "managementSettings provided but the running STExpressIntroductionSettingsDefaultsObjC does not support setManagementIsManaged:"
+ "saveExpressIntroductionSettingsDefaults:forUser:completionHandler:"
+ "saveExpressIntroductionSettingsDefaultsWithIsContentRestrictionsEnabled:contentRestrictionsByKey:isCommunicationSafetyEnabled:isScreenDistanceEnabled:isStrictPolicy:managementSettings:completionHandler:"
+ "setManagementHasStrictPolicy:"
+ "setManagementIsManaged:"
+ "setOperatingSystems:"
+ "setRestrictionsForAccountWithAdditionalHeaders:managementSettings:completion:"
+ "setRestrictionsForProtoAccount:managementSettings:completion:"
+ "v40@0:8@\"FAScreenTimeCoreSoftLinking\"16@\"FARestrictionsManagementSettings\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NSDictionary\"16@\"FARestrictionsManagementSettings\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?@\"AKDeviceListResponse\"@\"NSError\">32"
+ "v40@0:8Q16@\"FARestrictionsManagementSettings\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8Q16@24@?32"
+ "v48@0:8Q16@\"FARestrictionsManagementSettings\"24@\"FAScreenTimeCoreSoftLinking\"32@?<v@?B@\"NSError\">40"
+ "v56@0:8@\"FAScreenTimeCoreSoftLinking\"16@\"FASettingsPresetsRequest\"24@\"NSDictionary\"32@\"FARestrictionsManagementSettings\"40@?<v@?B@\"NSError\">48"
+ "v56@0:8B16@20B28B32B36@40@?48"
- "Applying account restrictions through ScreenTime settings."
- "Applying proto account restrictions (%lu) through ScreenTime settings."
- "Setting account restrictions through ST settings with additional headers."
- "Setting proto account restrictions (%lu) through ST settings."
- "applyDefaultRestrictionsForAccount(with:presetsRequest:additionalHeaders:)"
- "applyDefaultRestrictionsForAccountWithScreenTimeCore:presetsRequest:additionalHeaders:completion:"
- "applyDefaultRestrictionsForProtoAccountWithScreenTimeCore:completion:"
- "applyRestrictionsForProtoAccount(_:screenTimeCore:)"
- "applyRestrictionsForProtoAccount:screenTimeCore:completion:"
- "saveExpressIntroductionSettingsDefaultsWithIsContentRestrictionsEnabled:contentRestrictionsByKey:isCommunicationSafetyEnabled:isScreenDistanceEnabled:isStrictPolicy:completionHandler:"
- "setRestrictionsForAccountWithAdditionalHeaders:completion:"
- "setRestrictionsForProtoAccount:completion:"
- "v32@0:8Q16@?<v@?B@\"NSError\">24"
- "v40@0:8Q16@\"FAScreenTimeCoreSoftLinking\"24@?<v@?B@\"NSError\">32"
- "v48@0:8@\"FAScreenTimeCoreSoftLinking\"16@\"FASettingsPresetsRequest\"24@\"NSDictionary\"32@?<v@?B@\"NSError\">40"
- "v48@0:8B16@20B28B32B36@?40"
```
