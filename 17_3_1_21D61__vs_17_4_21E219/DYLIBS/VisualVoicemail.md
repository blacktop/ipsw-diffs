## VisualVoicemail

> `/System/Library/PrivateFrameworks/VisualVoicemail.framework/VisualVoicemail`

```diff

-785.0.0.0.0
-  __TEXT.__text: 0x15ca8
+801.2.0.0.0
+  __TEXT.__text: 0x15fd0
   __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x1878
+  __TEXT.__objc_methlist: 0x1888
   __TEXT.__cstring: 0xd62
   __TEXT.__gcc_except_tab: 0x360
-  __TEXT.__oslogstring: 0x11b4
+  __TEXT.__oslogstring: 0x1288
   __TEXT.__const: 0x30
-  __TEXT.__unwind_info: 0x748
+  __TEXT.__unwind_info: 0x750
   __TEXT.__objc_classname: 0x2b7
-  __TEXT.__objc_methname: 0x3de1
-  __TEXT.__objc_methtype: 0x96d
-  __TEXT.__objc_stubs: 0x2c60
+  __TEXT.__objc_methname: 0x3e59
+  __TEXT.__objc_methtype: 0x99b
+  __TEXT.__objc_stubs: 0x2c40
   __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x868
+  __DATA_CONST.__const: 0x890
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3888
-  __DATA_CONST.__objc_selrefs: 0x1010
+  __DATA_CONST.__objc_const: 0x38a8
+  __DATA_CONST.__objc_selrefs: 0x1018
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x198
+  __DATA_CONST.__objc_superrefs: 0x80
   __AUTH_CONST.__cfstring: 0xfa0
   __AUTH_CONST.__objc_const: 0x858
   __AUTH_CONST.__const: 0x240
   __AUTH_CONST.__auth_got: 0x338
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x198
-  __DATA.__objc_superrefs: 0x80
-  __DATA.__objc_ivar: 0x178
+  __DATA.__objc_ivar: 0x17c
   __DATA.__data: 0x610
-  __DATA.__bss: 0x28
+  __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x550
-  __DATA_DIRTY.__bss: 0x60
+  __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 676
-  Symbols:   2441
-  CStrings:  1170
+  Functions: 677
+  Symbols:   2444
+  CStrings:  1179
 
Symbols:
+ -[VMVoicemailManager _fetchInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]
+ -[VMVoicemailManager initAsyncWithStateSync:mailSync:session:delegate:delegateQueue:]
+ -[VMVoicemailManager initWithClient:synchronously:queryState:fetchMail:session:delegate:delegateQueue:]
+ -[VMVoicemailManager initWithStateSync:mailSync:delegate:delegateQueue:]
+ GCC_except_table128
+ GCC_except_table133
+ GCC_except_table136
+ GCC_except_table139
+ GCC_except_table142
+ GCC_except_table145
+ GCC_except_table152
+ GCC_except_table155
+ GCC_except_table164
+ GCC_except_table170
+ GCC_except_table176
+ GCC_except_table179
+ GCC_except_table22
+ GCC_except_table23
+ GCC_except_table28
+ GCC_except_table32
+ GCC_except_table62
+ GCC_except_table64
+ GCC_except_table66
+ GCC_except_table68
+ GCC_except_table70
+ GCC_except_table75
+ GCC_except_table79
+ GCC_except_table82
+ GCC_except_table9
+ _OBJC_IVAR_$_VMVoicemailManager.fSyncStateExpected
+ ___103-[VMVoicemailManager _fetchInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke
+ ___103-[VMVoicemailManager _fetchInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.15
+ ___103-[VMVoicemailManager _fetchInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.16
+ ___103-[VMVoicemailManager _fetchInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.16.cold.1
+ ___103-[VMVoicemailManager _fetchInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.17
+ ___103-[VMVoicemailManager _fetchInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.20
+ ___103-[VMVoicemailManager _fetchInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.21
+ ___103-[VMVoicemailManager _fetchInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.21.cold.1
+ ___103-[VMVoicemailManager _fetchInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.22
+ ___103-[VMVoicemailManager _fetchInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.25
+ ___103-[VMVoicemailManager _fetchInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.26
+ ___103-[VMVoicemailManager _fetchInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.26.cold.1
+ ___103-[VMVoicemailManager _fetchInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.27
+ ___103-[VMVoicemailManager _fetchInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke_2
+ ___103-[VMVoicemailManager _fetchInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke_2.23
+ ___103-[VMVoicemailManager _fetchInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke_2.28
+ ___103-[VMVoicemailManager _fetchInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke_3
+ ___103-[VMVoicemailManager initWithClient:synchronously:queryState:fetchMail:session:delegate:delegateQueue:]_block_invoke
+ ___35-[VMClientWrapper clientConnection]_block_invoke.166
+ ___35-[VMClientWrapper clientConnection]_block_invoke.166.cold.1
+ ___35-[VMClientWrapper clientConnection]_block_invoke.169
+ ___35-[VMClientWrapper clientConnection]_block_invoke.175
+ ___73-[VMVoicemailManager requestInitialStateIfNecessaryAndSendNotifications:]_block_invoke.12
+ ___block_descriptor_65_e8_32s40s48bs56w_e28_v16?0"VMVoicemailManager"8ls32l8w56l8s40l8s48l8
+ ___block_literal_global.11
+ ___block_literal_global.140
+ ___block_literal_global.160
+ ___block_literal_global.168
+ ___block_literal_global.172
+ _objc_msgSend$_fetchInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:
+ _objc_msgSend$initAsyncWithStateSync:mailSync:session:delegate:delegateQueue:
+ _objc_msgSend$initWithClient:synchronously:queryState:fetchMail:session:delegate:delegateQueue:
+ _objc_retain_x5
- -[VMVoicemailManager _requestInitialStateIfNecessaryWithForce:]
- -[VMVoicemailManager _requestInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]
- -[VMVoicemailManager initWithClient:synchronously:fetchMail:session:delegate:delegateQueue:]
- GCC_except_table127
- GCC_except_table132
- GCC_except_table135
- GCC_except_table138
- GCC_except_table141
- GCC_except_table144
- GCC_except_table151
- GCC_except_table154
- GCC_except_table163
- GCC_except_table169
- GCC_except_table175
- GCC_except_table178
- GCC_except_table20
- GCC_except_table21
- GCC_except_table26
- GCC_except_table30
- GCC_except_table61
- GCC_except_table63
- GCC_except_table65
- GCC_except_table67
- GCC_except_table69
- GCC_except_table7
- GCC_except_table74
- GCC_except_table78
- GCC_except_table81
- ___105-[VMVoicemailManager _requestInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke
- ___105-[VMVoicemailManager _requestInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.15
- ___105-[VMVoicemailManager _requestInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.16
- ___105-[VMVoicemailManager _requestInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.16.cold.1
- ___105-[VMVoicemailManager _requestInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.17
- ___105-[VMVoicemailManager _requestInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.20
- ___105-[VMVoicemailManager _requestInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.21
- ___105-[VMVoicemailManager _requestInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.21.cold.1
- ___105-[VMVoicemailManager _requestInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.22
- ___105-[VMVoicemailManager _requestInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.25
- ___105-[VMVoicemailManager _requestInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.26
- ___105-[VMVoicemailManager _requestInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.26.cold.1
- ___105-[VMVoicemailManager _requestInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke.27
- ___105-[VMVoicemailManager _requestInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke_2
- ___105-[VMVoicemailManager _requestInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke_2.23
- ___105-[VMVoicemailManager _requestInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke_2.28
- ___105-[VMVoicemailManager _requestInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:]_block_invoke_3
- ___35-[VMClientWrapper clientConnection]_block_invoke.165
- ___35-[VMClientWrapper clientConnection]_block_invoke.165.cold.1
- ___35-[VMClientWrapper clientConnection]_block_invoke.168
- ___35-[VMClientWrapper clientConnection]_block_invoke.174
- ___73-[VMVoicemailManager requestInitialStateIfNecessaryAndSendNotifications:]_block_invoke.10
- ___92-[VMVoicemailManager initWithClient:synchronously:fetchMail:session:delegate:delegateQueue:]_block_invoke
- ___block_literal_global.139
- ___block_literal_global.159
- ___block_literal_global.167
- ___block_literal_global.171
- ___block_literal_global.9
- _objc_msgSend$_requestInitialStateIfNecessaryWithForce:
- _objc_msgSend$_requestInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:
- _objc_msgSend$initWithClient:synchronously:fetchMail:session:delegate:delegateQueue:
- _objc_msgSend$requestInitialStateIfNecessaryAndSendNotifications:
- _objc_retain_x26
CStrings:
+ "%@ client initialized without expecting mail or states sync"
+ "@40@0:8B16B20@24@32"
+ "@48@0:8B16B20@24@32@40"
+ "@60@0:8@16B24B28B32@36@44@52"
+ "T@\"NSString\",?,R,C"
+ "_fetchInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:"
+ "fSyncStateExpected"
+ "initAsyncWithStateSync:mailSync:session:delegate:delegateQueue:"
+ "initWithClient:synchronously:queryState:fetchMail:session:delegate:delegateQueue:"
+ "initWithStateSync:mailSync:delegate:delegateQueue:"
+ "mail fetch is not requested - skipping to accounts"
+ "requested startMailSyncing - starting sync"
+ "requested startMailSyncing while it was already active - skipping"
+ "starting with statesync: %s, mailsync: %s"
- "%@ client initialized without expecting mail sync"
- "@56@0:8@16B24B28@32@40@48"
- "_requestInitialStateIfNecessaryWithForce:"
- "_requestInitialStateIfNecessaryWithForce:waitStates:waitMails:waitAccounts:session:"
- "initWithClient:synchronously:fetchMail:session:delegate:delegateQueue:"

```
