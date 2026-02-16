## EmbeddedDataReset

> `/System/Library/PrivateFrameworks/EmbeddedDataReset.framework/EmbeddedDataReset`

```diff

-56.3.1.0.0
-  __TEXT.__text: 0x2378
-  __TEXT.__auth_stubs: 0x300
+56.4.1.0.0
+  __TEXT.__text: 0x25c8
+  __TEXT.__auth_stubs: 0x2b0
   __TEXT.__objc_methlist: 0x45c
   __TEXT.__const: 0x80
   __TEXT.__cstring: 0x26f
-  __TEXT.__gcc_except_tab: 0x16c
+  __TEXT.__gcc_except_tab: 0x15c
   __TEXT.__oslogstring: 0x48c
-  __TEXT.__unwind_info: 0x100
+  __TEXT.__unwind_info: 0x118
   __TEXT.__objc_classname: 0xb6
   __TEXT.__objc_methname: 0xadc
   __TEXT.__objc_methtype: 0x286

   __DATA_CONST.__objc_selrefs: 0x318
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x190
+  __AUTH_CONST.__auth_got: 0x168
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x180
   __AUTH_CONST.__objc_const: 0x830

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CB7B4253-80DE-3763-BD8C-BDA536C03573
+  UUID: 95BAD882-813F-306F-8796-31895A041F46
   Functions: 67
-  Symbols:   366
+  Symbols:   361
   CStrings:  250
 
Symbols:
+ _objc_autoreleaseReturnValue
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_release_x25
- _objc_release_x26
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x21
- _objc_retain_x23
- _objc_retain_x8
Functions:
~ _DDRLogForCategory : 96 -> 104
~ +[DDRResetService sharedInstance] : 160 -> 176
~ ___33+[DDRResetService sharedInstance]_block_invoke : 172 -> 176
~ ___30-[DDRResetService addOberver:]_block_invoke : 492 -> 528
~ ___34-[DDRResetService removeObserver:]_block_invoke : 332 -> 352
~ -[DDRResetService observerNonLaunchingXPCConnection] : 676 -> 704
~ ___52-[DDRResetService observerNonLaunchingXPCConnection]_block_invoke : 136 -> 140
~ ___52-[DDRResetService observerNonLaunchingXPCConnection]_block_invoke.58 : 136 -> 140
~ -[DDRResetService dataResetXPCConnection] : 768 -> 796
~ ___41-[DDRResetService dataResetXPCConnection]_block_invoke : 136 -> 140
~ ___41-[DDRResetService dataResetXPCConnection]_block_invoke.72 : 136 -> 140
~ -[DDRResetService notifyClientsOfResetFailedWithErrorCode:] : 248 -> 256
~ -[DDRResetService resetWithRequest:completion:] : 928 -> 956
~ ___47-[DDRResetService resetWithRequest:completion:]_block_invoke : 248 -> 252
~ ___47-[DDRResetService resetWithRequest:completion:]_block_invoke.75 : 168 -> 172
~ -[DDRResetService invalidate] : 132 -> 136
~ -[DDRResetService willBeginDataResetWithMode:] : 544 -> 560
~ -[DDRResetService didBeginDataResetWithMode:] : 544 -> 560
~ -[DDRResetService didCompleteDataResetMode:withError:completion:] : 800 -> 808
~ -[DDRResetService setDataResetXPCConnection:] : 12 -> 64
~ -[DDRResetService setObserverNonLaunchingXPCConnection:] : 12 -> 64
~ -[DDRResetService setObervers:] : 12 -> 64
~ -[DDRResetService setObserverQueue:] : 12 -> 64
~ -[DDRResetOptions initWithCoder:] : 300 -> 312
~ -[DDRResetOptions encodeWithCoder:] : 280 -> 292
~ -[DDRResetOptions setBootstrapToken:] : 12 -> 64
~ -[DDRResetOptions setRevertToSnapshotName:] : 12 -> 64
~ -[DDRResetRequest initWithMode:options:reason:] : 160 -> 152
~ -[DDRResetRequest initWithCoder:] : 160 -> 172
~ -[DDRResetRequest encodeWithCoder:] : 128 -> 136

```
