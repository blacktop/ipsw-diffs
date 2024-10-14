## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-386.100.23.0.0
-  __TEXT.__text: 0x8b650
+386.100.23.7.0
+  __TEXT.__text: 0x8c394
   __TEXT.__auth_stubs: 0x1130
-  __TEXT.__objc_methlist: 0x4438
+  __TEXT.__objc_methlist: 0x445c
   __TEXT.__const: 0x6f0
-  __TEXT.__oslogstring: 0x13688
+  __TEXT.__oslogstring: 0x139c8
   __TEXT.__cstring: 0x7195
-  __TEXT.__gcc_except_tab: 0xb84
+  __TEXT.__gcc_except_tab: 0xb7c
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x2f5
   __TEXT.__swift5_fieldmd: 0x8c

   __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_capture: 0x1b8
-  __TEXT.__unwind_info: 0x1c50
+  __TEXT.__unwind_info: 0x1c88
   __TEXT.__eh_frame: 0x950
   __TEXT.__objc_classname: 0xc50
-  __TEXT.__objc_methname: 0xe9b0
+  __TEXT.__objc_methname: 0xea61
   __TEXT.__objc_methtype: 0x2928
-  __TEXT.__objc_stubs: 0xbd40
+  __TEXT.__objc_stubs: 0xbdc0
   __DATA_CONST.__got: 0xfb0
-  __DATA_CONST.__const: 0x2468
+  __DATA_CONST.__const: 0x2508
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x34c0
+  __DATA_CONST.__objc_selrefs: 0x34e0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x78

   __AUTH_CONST.__auth_ptr: 0x1d0
   __AUTH_CONST.__const: 0x988
   __AUTH_CONST.__cfstring: 0x4bc0
-  __AUTH_CONST.__objc_const: 0x11660
+  __AUTH_CONST.__objc_const: 0x11690
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1050

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2975
-  Symbols:   3772
-  CStrings:  4657
+  Functions: 2993
+  Symbols:   3793
+  CStrings:  4672
 
CStrings:
+ "\"%!@(MISSING): EDP state is good, clearing EDP followup!\""
+ "\"%!@(MISSING): Recovery Token needed, clearing EDP followup and post fix-all followup\""
+ "\"%!@(MISSING): Repair EDP State: %!l(MISSING)u, RT needed: %!d(MISSING), repair Error: %!@(MISSING)\""
+ "\"%!@(MISSING): Repair EDP State: %!l(MISSING)u, Recovery Token needed: %!d(MISSING), repair Error: %!@(MISSING)\""
+ "\"%!@(MISSING): User canceled the interactive auth during repairEDPStateWithCompletion. Error: %!@(MISSING), not offering recovery token yet\""
+ "\"Attempting to upload token with id: %!@(MISSING)\""
+ "\"CDP repair isn't needed\""
+ "\"EDP is good now, but CDP is broken and needs repair\""
+ "\"Failed to renew credentials for account with error %!@(MISSING)\""
+ "\"Renew Credentials failed - Primary account DSID (%!{(MISSING)mask.hash}@) does not match the DSID specified in the context (%!{(MISSING)mask.hash}@)\""
+ "\"Renew Credentials skipped for non-auth errors, returning result back to caller\""
+ "\"RepairEDP failed with authentication error: %!@(MISSING)\""
+ "\"User cancelled from the password prompt. Cancelling entire flow. Error: %!@(MISSING)\""
+ "\"User is Walrus enabled, will not use EDP Recovery Token as an escape offer...\""
+ "-[CDPDStateMachine _performEDPRepairWithResult:completion:]"
+ "_continuePerformEDPRepairWithCDPEnabled:completion:"
+ "_performEDPRepairWithResult:completion:"
+ "_renewCredentialsWithError:completion:"
+ "ak_isAuthenticationErrorWithCode:"
+ "clearCDPEDPFollowUp"
+ "isAuthenticationErrorIncludingUnderlyingErrors"
+ "refreshWithSilentAuthWithCompletion:"
- "\"Attempting to upload %!@(MISSING)\""
- "\"CDP repair isn't needed, we can tear down the CFU\""
- "\"User cancelled from the password prompt. Cancelling entire flow.\""
- "-[CDPDStateMachine _performEDPRepairWithCompletion:]"
- "_clearCDPEDPFollowUp"
- "_performEDPRepairWithCompletion:"
- "refreshWithSilentAuthWithCcompletion:"

```
