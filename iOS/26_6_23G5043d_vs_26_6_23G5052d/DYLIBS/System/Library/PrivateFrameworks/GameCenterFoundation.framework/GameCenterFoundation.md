## GameCenterFoundation

> `/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation`

```diff

-  __TEXT.__text: 0x18063c
-  __TEXT.__auth_stubs: 0x2890
+  __TEXT.__text: 0x180e58
+  __TEXT.__auth_stubs: 0x28b0
   __TEXT.__objc_methlist: 0x12494
-  __TEXT.__cstring: 0x18e20
+  __TEXT.__cstring: 0x19010
   __TEXT.__const: 0x65d8
-  __TEXT.__gcc_except_tab: 0x1410
-  __TEXT.__oslogstring: 0xdcfb
+  __TEXT.__gcc_except_tab: 0x1490
+  __TEXT.__oslogstring: 0xde1b
   __TEXT.__ustring: 0x18
   __TEXT.__dlopen_cstrs: 0xba
   __TEXT.__swift5_typeref: 0x1f88

   __TEXT.__swift_as_entry: 0x190
   __TEXT.__swift_as_ret: 0x1dc
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__unwind_info: 0x73e8
+  __TEXT.__unwind_info: 0x7420
   __TEXT.__eh_frame: 0x5a40
   __TEXT.__objc_classname: 0x25ad
   __TEXT.__objc_methname: 0x289a5
   __TEXT.__objc_methtype: 0x6b82
   __TEXT.__objc_stubs: 0x15860
   __DATA_CONST.__got: 0x1140
-  __DATA_CONST.__const: 0x6118
+  __DATA_CONST.__const: 0x6168
   __DATA_CONST.__objc_classlist: 0x828
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x230

   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x508
   __DATA_CONST.__objc_arraydata: 0x280
-  __AUTH_CONST.__auth_got: 0x1458
-  __AUTH_CONST.__const: 0x5a50
-  __AUTH_CONST.__cfstring: 0x116a0
+  __AUTH_CONST.__auth_got: 0x1468
+  __AUTH_CONST.__const: 0x5a90
+  __AUTH_CONST.__cfstring: 0x11920
   __AUTH_CONST.__objc_const: 0x24ff0
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_intobj: 0x288

   __AUTH.__data: 0x1128
   __DATA.__objc_ivar: 0x1068
   __DATA.__data: 0x3b28
-  __DATA.__bss: 0x8520
+  __DATA.__bss: 0x8530
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x2ba0
   __DATA_DIRTY.__data: 0x5e8

   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
   - /System/Library/PrivateFrameworks/CopresenceCore.framework/CopresenceCore
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/GameKitServices.framework/GameKitServices
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11052
-  Symbols:   25471
-  CStrings:  13720
+  Functions: 11057
+  Symbols:   25492
+  CStrings:  13765
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ GCC_except_table71
+ _DMIsMigrationNeeded
+ _DMPerformMigrationReturningAfterPlugin
+ _GKKickoffAccountsMigrationGate.once
+ ___54-[ACAccountStore(GameCenter) _gkMapAccountsWithBlock:]_block_invoke_3
+ ___GKKickoffAccountsMigrationGate_block_invoke
+ ___block_descriptor_40_e8_32s_e18_v16?0"NSString"8ls32l8
+ ___block_descriptor_64_e8_32s40s48bs56bs_e14_v16?0?<v?>8ls48l8s32l8s56l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e34_v32?0"NSNumber"8"NSArray"16^B24ls56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48bs56bs64bs_e35_v24?0"ACAccountType"8"NSError"16ls48l8s56l8s32l8s64l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56bs64bs72bs_e20_v20?0B8"NSError"12ls56l8s32l8s40l8s64l8s48l8s72l8
+ __gkAccountsMigrationDone
- GCC_except_table33
- ___block_descriptor_56_e8_32s40s48s_e34_v32?0"NSNumber"8"NSArray"16^B24ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48bs56bs_e35_v24?0"ACAccountType"8"NSError"16ls48l8s32l8s56l8s40l8
- ___block_descriptor_72_e8_32s40s48s56bs64bs_e20_v20?0B8"NSError"12ls32l8s40l8s56l8s48l8s64l8
CStrings:
+ "\n"
+ "  +%7.3fs %@ (%.1fms)"
+ "  +%7.3fs %@ (PENDING %.3fs)"
+ "AK.setAppleIDWithAltDSID.duplicate"
+ "AK.setAppleIDWithAltDSID.legacy"
+ "Waiting for com.apple.accounts.migrator before serving accountsd queries"
+ "_gkMapAccountsWithBlock: returning nil. com.apple.accounts.migrator has not finished yet"
+ "_gkMapAccountsWithBlock: timed out after %ds. Stages:\n%@"
+ "accountTypeWithIdentifier"
+ "accountsWithAccountType"
+ "block.perAccount"
+ "com.apple.accounts.migrator"
+ "com.apple.accounts.migrator finished; accountsd queries enabled"
+ "com.apple.gamed.accountsMigrationGate"
+ "dedup.AKAppleID.init"
+ "dedup.byUsername"
+ "dedup.removeAccount.duplicate"
+ "dedup.removeAccount.older"
+ "done.aboutToCall"
+ "done.errorBranch"
+ "perform.entered"
+ "removeAccount.duplicateAppleID"
+ "removeAccount.legacyMalformed"
+ "requestAccessToAccountsWithType"

```
