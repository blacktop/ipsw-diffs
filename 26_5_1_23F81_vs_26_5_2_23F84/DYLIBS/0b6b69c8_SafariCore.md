## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore`

```diff

-  __TEXT.__text: 0x14e2e0
-  __TEXT.__auth_stubs: 0x3310
-  __TEXT.__objc_methlist: 0xbf6c
+  __TEXT.__text: 0x14f6cc
+  __TEXT.__auth_stubs: 0x3300
+  __TEXT.__objc_methlist: 0xbf7c
   __TEXT.__const: 0x3570
-  __TEXT.__gcc_except_tab: 0x709c
+  __TEXT.__gcc_except_tab: 0x7100
   __TEXT.__cstring: 0x130e5
   __TEXT.__ustring: 0x2826
   __TEXT.__oslogstring: 0xb163

   __TEXT.__swift_as_ret: 0xf4
   __TEXT.__swift5_capture: 0x70c
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x6a28
+  __TEXT.__unwind_info: 0x6a90
   __TEXT.__eh_frame: 0x3a00
   __TEXT.__objc_classname: 0x1de5
-  __TEXT.__objc_methname: 0x261d5
+  __TEXT.__objc_methname: 0x26125
   __TEXT.__objc_methtype: 0x46aa
   __TEXT.__objc_stubs: 0x12c20
   __DATA_CONST.__got: 0xea0
-  __DATA_CONST.__const: 0x5258
+  __DATA_CONST.__const: 0x52a8
   __DATA_CONST.__objc_classlist: 0x610
   __DATA_CONST.__objc_catlist: 0x160
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6e10
+  __DATA_CONST.__objc_selrefs: 0x6e18
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x4a0
   __DATA_CONST.__objc_arraydata: 0x2a20
-  __AUTH_CONST.__auth_got: 0x19a0
-  __AUTH_CONST.__const: 0x6c08
+  __AUTH_CONST.__auth_got: 0x1998
+  __AUTH_CONST.__const: 0x6c28
   __AUTH_CONST.__cfstring: 0x19ba0
-  __AUTH_CONST.__objc_const: 0x13ac8
+  __AUTH_CONST.__objc_const: 0x13b48
   __AUTH_CONST.__objc_intobj: 0x870
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x5a0
   __AUTH.__objc_data: 0x2710
   __AUTH.__data: 0x660
-  __DATA.__objc_ivar: 0xc74
+  __DATA.__objc_ivar: 0xc84
   __DATA.__data: 0x1a58
   __DATA.__bss: 0x5190
   __DATA.__common: 0x30

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8010
-  Symbols:   21397
-  CStrings:  13327
+  Functions: 8035
+  Symbols:   21457
+  CStrings:  13324
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__eh_frame : content changed
~ __TEXT.__objc_classname : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ +[WBSTOTPGenerator keyDataForBase32EncodedString:]
+ +[WBSTOTPGenerator keyDataForBase32EncodedString:].cold.1
+ -[WBSAutoFillQuirksManager test_waitForInternalQueueToEmpty]
+ _OBJC_IVAR_$_WBSAppIDsToDomainsAssociationManager._queue
+ _OBJC_IVAR_$_WBSChangePasswordURLManager._queue
+ _OBJC_IVAR_$_WBSPasswordAuditingEligibleDomainsManager._queue
+ _OBJC_IVAR_$_WBSPasswordGenerationManager._queue
+ ___50+[WBSTOTPGenerator keyDataForBase32EncodedString:]_block_invoke
+ ___51-[WBSAppIDsToDomainsAssociationManager description]_block_invoke
+ ___53-[WBSPasswordGenerationManager passwordRulesByDomain]_block_invoke
+ ___55-[WBSAppIDsToDomainsAssociationManager appIDsToDomains]_block_invoke
+ ___55-[WBSChangePasswordURLManager changePasswordURLStrings]_block_invoke
+ ___57-[WBSPasswordGenerationManager setPasswordRulesByDomain:]_block_invoke
+ ___59-[WBSAppIDsToDomainsAssociationManager setAppIDsToDomains:]_block_invoke
+ ___59-[WBSChangePasswordURLManager setChangePasswordURLStrings:]_block_invoke
+ ___60-[WBSAutoFillQuirksManager test_waitForInternalQueueToEmpty]_block_invoke
+ ___60-[WBSPasswordGenerationManager passwordRequirementsByDomain]_block_invoke
+ ___61-[WBSPasswordGenerationManager defaultRequirementsForDomain:]_block_invoke
+ ___62-[WBSPasswordGenerationManager defaultPasswordRulesForDomain:]_block_invoke
+ ___64-[WBSPasswordGenerationManager setPasswordRequirementsByDomain:]_block_invoke
+ ___67-[WBSChangePasswordURLManager changePasswordURLForHighLevelDomain:]_block_invoke
+ ___81-[WBSAppIDsToDomainsAssociationManager domainsWithAssociatedCredentialsForAppID:]_block_invoke
+ ___81-[WBSPasswordAuditingEligibleDomainsManager domainsIneligibleForPasswordAuditing]_block_invoke
+ ___85-[WBSPasswordAuditingEligibleDomainsManager setDomainsIneligibleForPasswordAuditing:]_block_invoke
+ ___block_descriptor_48_ea8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_56_ea8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_literal_global.35
+ _keyDataForBase32EncodedString:.inverseAlphabet
+ _keyDataForBase32EncodedString:.onceToken
+ _objc_msgSend$keyDataForBase32EncodedString:
- +[WBSTOTPGenerator _keyDataForBase32EncodedString:]
- +[WBSTOTPGenerator _keyDataForBase32EncodedString:].cold.1
- GCC_except_table50
- ___51+[WBSTOTPGenerator _keyDataForBase32EncodedString:]_block_invoke
- ___block_literal_global.161
- __keyDataForBase32EncodedString:.inverseAlphabet
- __keyDataForBase32EncodedString:.onceToken
- _objc_msgSend$_keyDataForBase32EncodedString:
- _objc_setProperty_atomic_copy
CStrings:
+ "T@\"NSDictionary\",C"
+ "T@\"NSSet\",C"
+ "keyDataForBase32EncodedString:"
+ "test_waitForInternalQueueToEmpty"
- "\""
- "T@\"NSDictionary\",C,N,V_appIDsToDomains"
- "T@\"NSDictionary\",C,N,V_passwordRequirementsByDomain"
- "T@\"NSDictionary\",C,N,V_passwordRulesByDomain"
- "T@\"NSDictionary\",C,V_changePasswordURLStrings"
- "T@\"NSSet\",C,V_domainsIneligibleForPasswordAuditing"
- "_keyDataForBase32EncodedString:"

```
