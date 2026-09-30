## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

```diff

-905.120.4.0.0
-  __TEXT.__text: 0xaddb8
+905.140.2.0.0
+  __TEXT.__text: 0xadea8
   __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_methlist: 0xaafc
-  __TEXT.__cstring: 0x1f219
-  __TEXT.__const: 0x2b0
+  __TEXT.__objc_methlist: 0xab14
+  __TEXT.__cstring: 0x1f331
+  __TEXT.__const: 0x2a8
   __TEXT.__gcc_except_tab: 0x1078
   __TEXT.__oslogstring: 0xd81
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__unwind_info: 0x3168
   __TEXT.__objc_classname: 0xed4
-  __TEXT.__objc_methname: 0x186d3
+  __TEXT.__objc_methname: 0x18704
   __TEXT.__objc_methtype: 0x34c9
-  __TEXT.__objc_stubs: 0x13d80
+  __TEXT.__objc_stubs: 0x13dc0
   __DATA_CONST.__got: 0xd60
   __DATA_CONST.__const: 0x2940
   __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5b08
+  __DATA_CONST.__objc_selrefs: 0x5b18
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x318
   __DATA_CONST.__objc_arraydata: 0xd8
   __AUTH_CONST.__auth_got: 0x7a0
   __AUTH_CONST.__const: 0x7c0
-  __AUTH_CONST.__cfstring: 0x12a80
-  __AUTH_CONST.__objc_const: 0x155d0
+  __AUTH_CONST.__cfstring: 0x12b20
+  __AUTH_CONST.__objc_const: 0x155e0
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x120

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 2F443938-97AF-3C29-8D76-16F04F3664C2
-  Functions: 4398
-  Symbols:   14704
-  CStrings:  9938
+  UUID: 3E94E7B9-A6D8-3093-8CD0-641AE1128BE0
+  Functions: 4400
+  Symbols:   14710
+  CStrings:  9951
 
Symbols:
+ -[SUPreferences inboxUpdaterdInitiatedScan]
+ -[SUScanOptions(SUS) clientIsInboxUpdaterd]
+ GCC_except_table82
+ GCC_except_table90
+ _objc_msgSend$clientIsInboxUpdaterd
+ _objc_msgSend$inboxUpdaterdInitiatedScan
- GCC_except_table76
- GCC_except_table89
Functions:
~ -[SUPreferences init] : 5704 -> 5764
+ -[SUScanOptions(SUS) clientIsInboxUpdaterd]
~ -[SUScanner scanForUpdates:shouldUseDDMInState:complete:] : 1160 -> 1204
~ +[SUUtility autoDownloadTimeInterval] : 216 -> 180
+ -[SUPreferences spaceOverrideNeedMobileAssetSuspend]
CStrings:
+ "%s: Overriding result to YES by SUInboxUpdaterdInitiatedScan"
+ "%s: client is inboxupdaterd; disable splombo and psus for this scan"
+ "-[SUScanOptions(SUS) clientIsInboxUpdaterd]"
+ "SUInboxUpdaterdInitiatedScan"
+ "[Auto scan] Beta: Downloading every 1 day"
+ "clientIsInboxUpdaterd"
+ "com.apple.inboxupdaterd"
+ "if set to true, scans will be initiated with inboxupdaterd"
+ "inboxUpdaterdInitiatedScan"
- "[Auto scan] Customer: Downloading every 5 days"

```
