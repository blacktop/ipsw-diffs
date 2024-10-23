## threadradiod

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod`

```diff

-263.0.4.0.0
-  __TEXT.__text: 0x3cbe18
+265.0.3.0.0
+  __TEXT.__text: 0x3cbb34
   __TEXT.__auth_stubs: 0x11140
-  __TEXT.__objc_stubs: 0x94a0
+  __TEXT.__objc_stubs: 0x94c0
   __TEXT.__init_offsets: 0x9c
-  __TEXT.__objc_methlist: 0x5d60
+  __TEXT.__objc_methlist: 0x5d68
   __TEXT.__objc_classname: 0x5f4
   __TEXT.__const: 0x808b
-  __TEXT.__gcc_except_tab: 0x28c6c
-  __TEXT.__objc_methname: 0xe6b0
-  __TEXT.__cstring: 0x2ce74
-  __TEXT.__oslogstring: 0x20b5b
+  __TEXT.__gcc_except_tab: 0x28c68
+  __TEXT.__objc_methname: 0xe6c8
+  __TEXT.__cstring: 0x2ccf1
+  __TEXT.__oslogstring: 0x20c34
   __TEXT.__objc_methtype: 0x44f1
-  __TEXT.__unwind_info: 0x7680
+  __TEXT.__unwind_info: 0x7698
   __DATA_CONST.__auth_got: 0x88b8
   __DATA_CONST.__got: 0x900
   __DATA_CONST.__auth_ptr: 0x60
   __DATA_CONST.__const: 0xae40
-  __DATA_CONST.__cfstring: 0x56e0
+  __DATA_CONST.__cfstring: 0x5700
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA.__objc_const: 0x9130
-  __DATA.__objc_selrefs: 0x3458
+  __DATA.__objc_selrefs: 0x3460
   __DATA.__objc_ivar: 0x530
   __DATA.__objc_data: 0xe60
   __DATA.__data: 0x5c0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libdns_services.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 15872
-  Symbols:   81304
-  CStrings:  11745
+  Functions: 15877
+  Symbols:   81294
+  CStrings:  11747
 
Symbols:
+ -[ThreadNetworkManagerInstance(SM_extension) clearProvideEmacTracker].cold.1
+ -[ThreadNetworkManagerInstance(SM_extension) eraseKeyFromProvideEmacTracker:].cold.1
+ -[ThreadNetworkManagerInstance(SM_extension) printProvideEmacTracker]
+ GCC_except_table176
+ GCC_except_table179
+ GCC_except_table198
+ GCC_except_table220
+ GCC_except_table227
+ GCC_except_table250
+ GCC_except_table297
+ _Z34getBoolValue_isStateMachineEnabledv.cold.1
+ _Z34getBoolValue_isStateMachineEnabledv.cold.2
+ _Z42getBoolValue_isAudioNoThreadFeatureEnabledv.cold.1
+ _Z42getBoolValue_isAudioNoThreadFeatureEnabledv.cold.2
+ _Z43getBoolValue_isThreadAlwaysOnFeatureEnabledv.cold.1
+ _Z43getBoolValue_isThreadAlwaysOnFeatureEnabledv.cold.2
+ __ZN2ot3Mle3Mle27isThreadStateMachineEnabledEv
+ __block_descriptor_tmp.184
+ __block_descriptor_tmp.189
+ _objc_msgSend$printProvideEmacTracker
- GCC_except_table246
- GCC_except_table283
- GCC_except_table353
- _ZN16XPCIPCAPI_v1_rcp26interface_prop_get_handlerEPvNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEN8dispatch8callbackIU13block_pointerFvhN3xpc4dictEEEE.cold.5
- _ZN16XPCIPCAPI_v1_rcp26interface_prop_get_handlerEPvNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEN8dispatch8callbackIU13block_pointerFvhN3xpc4dictEEEE.cold.6
- __ZN14RcpHostContext39overrideAudioNoThreadFeatureDisablementEb
- __ZN14RcpHostContext41overrideWedStateMachineFeatureDisablementEb
- __ZN2ot3Mle3Mle14GenerateMleIidEv
- __block_descriptor_tmp.185
- __block_descriptor_tmp.190
- _otLinkRegenerateMleIid
- _otPlatVendorStateMachineWedEnabled
CStrings:
+ " Morty_Version: V0.265.0.2"
+ "%!s(MISSING):"
+ "%!s(MISSING): Already erase complete, wedAddr=[%!s(MISSING)], Wed Status=[%!s(MISSING)]"
+ "%!s(MISSING): Clear mWasChild for new home setting file."
+ "%!s(MISSING): Read NetworkInfo failed, error=%!s(MISSING)."
+ "%!s(MISSING): [%!s(MISSING)]:Fallback to Frameworks, keyPresent = %!s(MISSING), Value = %!d(MISSING)"
+ "%!s(MISSING): [%!s(MISSING)]:KEY_NOT_FOUND in Frameworks"
+ "%!s(MISSING): [%!s(MISSING)]:KEY_NOT_FOUND in Preferences"
+ "%!s(MISSING): erase wedAddr=[%!s(MISSING)]"
+ "%!s(MISSING): key=[%!s(MISSING)], value=[%!d(MISSING)]"
+ "-[ThreadNetworkManagerInstance(SM_extension) clearProvideEmacTracker]"
+ "-[ThreadNetworkManagerInstance(SM_extension) eraseKeyFromProvideEmacTracker:]"
+ "-[ThreadNetworkManagerInstance(SM_extension) printProvideEmacTracker]"
+ "/System/Library/PrivateFrameworks/CoreThreadRadio.framework/com.apple.threadradiodData.plist"
+ "MleRouter::HandleChildRequest: Rx linkFrameCounter=%!d(MISSING) mleFrameCounter=%!d(MISSING)"
+ "getBoolValue_isAudioNoThreadFeatureEnabled"
+ "getBoolValue_isStateMachineEnabled"
+ "getBoolValue_isThreadAlwaysOnFeatureEnabled"
+ "printProvideEmacTracker"
- " Morty_Version: V0.263.0.4"
- "%!s(MISSING) Authoritative MLE msg with keySeq:%!u(MISSING), mCurrSeq:%!u(MISSING) received, update keysequence"
- "%!s(MISSING) Neighbor KeySequence changed RLOC16: 0x%!x(MISSING), ExtAddr: %!s(MISSING), ourKeySeq:%!u(MISSING), nbrCurKeySeq:%!u(MISSING), nbrTableKeySeq:%!u(MISSING)"
- "%!s(MISSING) Neighbor KeySequence is lower than previous RLOC16: 0x%!x(MISSING), ExtAddr: %!s(MISSING), ourKeySeq:%!u(MISSING), nbrCurKeySeq:%!u(MISSING), nbrPrevKeySeq:%!u(MISSING)"
- "%!s(MISSING) Peer MLE msg with keySeq:%!u(MISSING) mCurrSeq:%!u(MISSING) received, update keysequence"
- "%!s(MISSING) Rotation time hoursSinceKeyRotation:%!u(MISSING), securityPolicy.RotationTime:%!u(MISSING), guardTimeSwitchEnabled:%!d(MISSING), guardTime:%!u(MISSING), keySequence:%!u(MISSING), isRunning:%!d(MISSING)"
- "%!s(MISSING) Rx from %!s(MISSING) linkFrameCounter=%!d(MISSING) mleFrameCounter=%!d(MISSING)"
- "%!s(MISSING) Unknown MLE msg with keySeq:%!u(MISSING), mCurrSeq:%!u(MISSING) received"
- "%!s(MISSING) Update keysequence as key rotation timer expired hoursSinceKeyRotation:%!u(MISSING), securityPolicy.RotationTime:%!u(MISSING), guardTimeSwitchEnabled:%!d(MISSING), guardTime:%!u(MISSING), keySequence:%!u(MISSING), isRunning:%!d(MISSING)"
- "%!s(MISSING): reconnect_thread_network"
- "HandleKeyRotationTimer"
- "HandleParentResponse"
- "MatteriPhoneOnlyPairingForiPad"
- "ProcessKeySequence"
- "ProcessReceiveSecurity"
- "Thread:Reconnect"
- "interface_prop_get_handler"

```
