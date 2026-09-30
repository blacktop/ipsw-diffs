## Email

> `/System/Library/PrivateFrameworks/Email.framework/Versions/A/Email`

```diff

-3826.500.181.1.5
-  __TEXT.__text: 0xea888
+3826.600.15.1.1
+  __TEXT.__text: 0xeaa70
   __TEXT.__auth_stubs: 0xd70
-  __TEXT.__objc_methlist: 0xd614
-  __TEXT.__gcc_except_tab: 0x1d474
+  __TEXT.__objc_methlist: 0xd624
+  __TEXT.__gcc_except_tab: 0x1d4b8
   __TEXT.__const: 0x36a
-  __TEXT.__cstring: 0xa3d9
+  __TEXT.__cstring: 0xa449
   __TEXT.__oslogstring: 0x6363
   __TEXT.__ustring: 0x154
   __TEXT.__dlopen_cstrs: 0x5e

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
   __TEXT.__unwind_info: 0x8320
-  __TEXT.__objc_classname: 0x1c4f
-  __TEXT.__objc_methname: 0x1c2d9
-  __TEXT.__objc_methtype: 0x4df7
-  __TEXT.__objc_stubs: 0x127a0
+  __TEXT.__objc_classname: 0x1c4c
+  __TEXT.__objc_methname: 0x1c395
+  __TEXT.__objc_methtype: 0x4dfd
+  __TEXT.__objc_stubs: 0x127c0
   __DATA_CONST.__got: 0xbd8
-  __DATA_CONST.__const: 0x17e8
+  __DATA_CONST.__const: 0x1800
   __DATA_CONST.__objc_classlist: 0x5a0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x350
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6038
+  __DATA_CONST.__objc_selrefs: 0x6040
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x490
   __DATA_CONST.__objc_arraydata: 0x1d0
   __AUTH_CONST.__auth_got: 0x6c8
   __AUTH_CONST.__auth_ptr: 0x90
   __AUTH_CONST.__const: 0x4e00
-  __AUTH_CONST.__cfstring: 0x9580
-  __AUTH_CONST.__objc_const: 0x17b10
+  __AUTH_CONST.__cfstring: 0x9600
+  __AUTH_CONST.__objc_const: 0x17b40
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x1ce0
   __AUTH.__data: 0x40
-  __DATA.__objc_ivar: 0xcc4
+  __DATA.__objc_ivar: 0xcc8
   __DATA.__data: 0x2820
   __DATA.__bss: 0x6b0
   __DATA_DIRTY.__objc_data: 0x1c70

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4820
-  Symbols:   14154
-  CStrings:  7329
+  Functions: 4821
+  Symbols:   14160
+  CStrings:  7335
 
Symbols:
+ +[EMListUnsubscribeCommand mailtoUnsubscribeCommandWithListID:address:sender:senderForUnsubscribeMessage:subject:body:account:headerUnsubscribeTypes:]
+ +[EMListUnsubscribeCommand oneClickUnsubscribeCommandWithListID:sender:senderForUnsubscribeMessage:URL:postContent:headerUnsubscribeTypes:]
+ -[EMListUnsubscribeCommand initWithListID:sender:senderForUnsubscribeMessage:mailtoValues:postValues:headerUnsubscribeTypes:]
+ -[EMListUnsubscribeCommand senderForUnsubscribeMessage]
+ OBJC_IVAR_$_EMListUnsubscribeCommand._senderForUnsubscribeMessage
+ _EMPersistenceStatisticsKeyMessagesToRedonate
+ _EMPersistenceStatisticsKeyPercentUnindexedBodiesInFrecentMailboxes
+ _EMPersistenceStatisticsKeyRemoteMessagesToRedonate
+ __53-[EMDiagnosticInfoGatherer initWithRemoteConnection:]_block_invoke.111
+ __59-[EMDiagnosticInfoGatherer registerDiagnosticInfoProvider:]_block_invoke.188
+ __68-[EMDiagnosticInfoGatherer provideDiagnosticsAt:options:completion:]_block_invoke.198
+ __68-[EMDiagnosticInfoGatherer provideDiagnosticsAt:options:completion:]_block_invoke.200
+ __68-[EMDiagnosticInfoGatherer provideDiagnosticsAt:options:completion:]_block_invoke.204
+ _objc_msgSend$initWithListID:sender:senderForUnsubscribeMessage:mailtoValues:postValues:headerUnsubscribeTypes:
+ _objc_msgSend$mailtoUnsubscribeCommandWithListID:address:sender:senderForUnsubscribeMessage:subject:body:account:headerUnsubscribeTypes:
+ _objc_msgSend$oneClickUnsubscribeCommandWithListID:sender:senderForUnsubscribeMessage:URL:postContent:headerUnsubscribeTypes:
+ _objc_msgSend$senderForUnsubscribeMessage
- +[EMListUnsubscribeCommand mailtoUnsubscribeCommandWithListID:address:sender:subject:body:account:headerUnsubscribeTypes:]
- +[EMListUnsubscribeCommand oneClickUnsubscribeCommandWithListID:sender:URL:postContent:headerUnsubscribeTypes:]
- -[EMListUnsubscribeCommand initWithListID:sender:mailtoValues:postValues:headerUnsubscribeTypes:]
- __53-[EMDiagnosticInfoGatherer initWithRemoteConnection:]_block_invoke.102
- __59-[EMDiagnosticInfoGatherer registerDiagnosticInfoProvider:]_block_invoke.179
- __68-[EMDiagnosticInfoGatherer provideDiagnosticsAt:options:completion:]_block_invoke.189
- __68-[EMDiagnosticInfoGatherer provideDiagnosticsAt:options:completion:]_block_invoke.191
- __68-[EMDiagnosticInfoGatherer provideDiagnosticsAt:options:completion:]_block_invoke.195
- _objc_msgSend$initWithListID:sender:mailtoValues:postValues:headerUnsubscribeTypes:
- _objc_msgSend$mailtoUnsubscribeCommandWithListID:address:sender:subject:body:account:headerUnsubscribeTypes:
- _objc_msgSend$oneClickUnsubscribeCommandWithListID:sender:URL:postContent:headerUnsubscribeTypes:
CStrings:
+ "% unindexed bodies in frecent"
+ "@64@0:8@16@24@32@40@48q56"
+ "@80@0:8@16@24@32@40@48@56@64q72"
+ "EFPropertyKey_senderForUnsubscribeMessage"
+ "T@\"NSString\",R,N,V_senderForUnsubscribeMessage"
+ "_senderForUnsubscribeMessage"
+ "initWithListID:sender:senderForUnsubscribeMessage:mailtoValues:postValues:headerUnsubscribeTypes:"
+ "mailtoUnsubscribeCommandWithListID:address:sender:senderForUnsubscribeMessage:subject:body:account:headerUnsubscribeTypes:"
+ "messagesToRedonate"
+ "oneClickUnsubscribeCommandWithListID:sender:senderForUnsubscribeMessage:URL:postContent:headerUnsubscribeTypes:"
+ "remoteMessagesToRedonate"
+ "senderForUnsubscribeMessage"
- "\x02\x12"
- "@56@0:8@16@24@32@40q48"
- "@72@0:8@16@24@32@40@48@56q64"
- "initWithListID:sender:mailtoValues:postValues:headerUnsubscribeTypes:"
- "mailtoUnsubscribeCommandWithListID:address:sender:subject:body:account:headerUnsubscribeTypes:"
- "oneClickUnsubscribeCommandWithListID:sender:URL:postContent:headerUnsubscribeTypes:"

```
