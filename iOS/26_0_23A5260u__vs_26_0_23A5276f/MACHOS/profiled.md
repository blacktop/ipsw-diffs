## profiled

> `/usr/libexec/profiled`

```diff

-2420.1.1.0.0
-  __TEXT.__text: 0xa0064
-  __TEXT.__auth_stubs: 0x20e0
-  __TEXT.__objc_stubs: 0x10520
-  __TEXT.__objc_methlist: 0x5a9c
+2422.0.0.0.0
+  __TEXT.__text: 0xa0238
+  __TEXT.__auth_stubs: 0x20d0
+  __TEXT.__objc_stubs: 0x10580
+  __TEXT.__objc_methlist: 0x5aac
   __TEXT.__const: 0x20e
-  __TEXT.__gcc_except_tab: 0x1bf8
-  __TEXT.__oslogstring: 0xd717
-  __TEXT.__cstring: 0x89c2
-  __TEXT.__objc_methname: 0x14470
-  __TEXT.__objc_classname: 0xb59
-  __TEXT.__objc_methtype: 0x224b
-  __TEXT.__unwind_info: 0x16f8
-  __DATA_CONST.__auth_got: 0x1080
+  __TEXT.__gcc_except_tab: 0x1bec
+  __TEXT.__oslogstring: 0xd736
+  __TEXT.__cstring: 0x8a12
+  __TEXT.__objc_methname: 0x144f0
+  __TEXT.__objc_classname: 0xb5b
+  __TEXT.__objc_methtype: 0x2239
+  __TEXT.__unwind_info: 0x1700
+  __DATA_CONST.__auth_got: 0x1078
   __DATA_CONST.__got: 0x1bb8
   __DATA_CONST.__const: 0x1b90
   __DATA_CONST.__cfstring: 0x85c0

   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x6568
-  __DATA.__objc_selrefs: 0x48d0
-  __DATA.__objc_ivar: 0x1fc
+  __DATA.__objc_const: 0x6580
+  __DATA.__objc_selrefs: 0x48d8
+  __DATA.__objc_ivar: 0x200
   __DATA.__objc_data: 0x1c70
   __DATA.__data: 0x540
   __DATA.__common: 0x20

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3719F0A3-AC1C-3603-B13C-F2CF88AFF8A3
-  Functions: 2038
-  Symbols:   1459
-  CStrings:  6129
+  UUID: FBD86B3F-72FF-36A7-936B-84BEEC5D1469
+  Functions: 2043
+  Symbols:   1458
+  CStrings:  6134
 
Symbols:
- _objc_retain_x6
CStrings:
+ "-[MCInteractionClient requestCurrentPasscodeOutExtractablePasscodeContext:]"
+ "-[MCInteractionClient requestCurrentPasscodeOutPasscodeContext:]"
+ "@\"MCExtractablePasscodeContextWrapper\""
+ "B28@0:8B16^@20"
+ "T@\"MCExtractablePasscodeContextWrapper\",&,N,V_passcodeContextWrapper"
+ "Updating CloudConfigUIComplete, CloudConfigWasApplied, and PostSetupProfileWasInstalled keys for set aside details."
+ "_passcodeContextWrapper"
+ "_requestCurrentPasscodeExtractable:outPasscodeContext:"
+ "createEnterprisePersonaWithPasscodeData:passcodeDataType:error:"
+ "didEnrollInMDMWithPasscodeContext:duringMigration:"
+ "doMCICDidRequestCurrentPasscodeNeedsExtractable:withCompletion:"
+ "generateAndSyncBootstrapTokenWithPasscode:passcodeContext:completionHandler:"
+ "installEnrollmentProfile:devicePasscode:devicePasscodeContext:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:managedProfileIdentifiers:installationSource:completionHandler:"
+ "passcodeContextWrapper"
+ "requestCurrentPasscodeOutExtractablePasscodeContext:"
+ "requestCurrentPasscodeOutPasscodeContext:"
+ "setPasscodeContextWrapper:"
+ "v36@?0B8@\"NSString\"12@\"NSData\"20@\"NSError\"28"
+ "v40@0:8@\"NSString\"16@\"NSData\"24@?<v@?B@\"NSError\">32"
+ "v92@0:8@\"NSData\"16@\"NSString\"24@\"NSData\"32@\"NSString\"40@\"NSString\"48B56@\"NSNumber\"60@\"NSArray\"68@\"NSString\"76@?<v@?@\"NSString\"B@\"NSError\">84"
+ "v92@0:8@16@24@32@40@48B56@60@68@76@?84"
- "-[MCInteractionClient requestCurrentPasscodeOutPasscodeContextWrapper:]"
- "Updating CloudConfigUIComplete and CloudConfigWasApplied keys for set aside details."
- "createBootstrapTokenIfNeededWithPasscode:completionHandler:"
- "createEnterprisePersonaWithDevicePasscode:error:"
- "deleteBootstrapTokenWithBootstrapToken:passcode:completionHandler:"
- "didEnrollInMDMWithPasscode:duringMigration:"
- "doMCICDidRequestCurrentPasscodeWithCompletion:"
- "installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:completionHandler:"
- "installEnrollmentProfile:devicePasscode:personaID:rmAccountIdentifier:isESSO:essoAppITunesStoreID:managedProfileIdentifiers:installationSource:completionHandler:"
- "requestCurrentPasscodeOutPasscodeContextWrapper:"
- "syncBootstrapToken:completionHandler:"
- "v28@?0B8@\"NSString\"12@\"NSError\"20"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v56@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@?<v@?@\"NSString\"B@\"NSError\">48"
- "v84@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40B48@\"NSNumber\"52@\"NSArray\"60@\"NSString\"68@?<v@?@\"NSString\"B@\"NSError\">76"
- "v84@0:8@16@24@32@40B48@52@60@68@?76"

```
