## HDAInterface

> `/System/Library/PrivateFrameworks/HDAInterface.framework/Versions/A/HDAInterface`

```diff

 600.2.0.0.0
-  __TEXT.__text: 0x8074
+  __TEXT.__text: 0x8030
   __TEXT.__auth_stubs: 0x2d0
   __TEXT.__objc_methlist: 0x874
   __TEXT.__cstring: 0x2cf5
-  __TEXT.__const: 0x30
-  __TEXT.__unwind_info: 0x220
+  __TEXT.__const: 0x40
+  __TEXT.__unwind_info: 0x210
   __TEXT.__objc_classname: 0xb6
   __TEXT.__objc_methname: 0x16d7
   __TEXT.__objc_methtype: 0x828

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EC9F5BB9-6670-37F4-A4C2-A0E0092A2000
-  Functions: 170
+  UUID: AD1D6859-1251-307E-BD3E-0331206FB908
+  Functions: 168
   Symbols:   410
   CStrings:  516
 
Functions:
~ +[HDAAudioEngineUserClient audioEngineUserClientForDeviceType:] : 84 -> 128
- sub_2364b4e90
~ -[HDADSPInterface setupSpeakerDSPForMeasurement:bypass_nonlinear:verbose:] : 768 -> 772
~ +[HDADSPUserClient dspUserClientForDeviceType:] : 84 -> 128
- sub_2364b79e4
~ -[HDADSPUserClient restoreFromDSPBypassState:withError:] : 408 -> 404
~ -[HDADSPUserClient setOutputMuteForChannel1:channel2:channel3:channel4:channel5:channel6:withError:] : 988 -> 980
~ -[HDADSPUserClient getOutputMuteForChannel1:channel2:channel3:channel4:channel5:channel6:withError:] : 1296 -> 1248
~ -[HDAMikeyInterface setupNewUserClient:builtIn:] : 664 -> 676
~ -[IOHDAudioCodecDeviceUserClient init] : 104 -> 96
~ -[IOHDAudioCodecDeviceUserClient SetupUserClient:index:] : 656 -> 648
~ -[IOHDAudioCodecDeviceUserClient SetupUserClientForDiag] : 568 -> 548
~ -[IOHDAudioCodecDeviceUserClient checkCodecExistsForController:Vendor:] : 332 -> 320
~ -[IOHDAudioCodecDeviceUserClient getCountOfUserClients:] : 184 -> 180
~ -[IOHDAudioCodecDeviceUserClient getHDAInterruptCountInfo] : 140 -> 136
~ -[IOHDAudioCodecDeviceUserClient readElapsedHighDefinitionAudioControllerRegisters] : 220 -> 224
~ -[IOHDAudioCodecDeviceUserClient readHighDefintionAudioControllerStickyStatus:] : 164 -> 168
~ -[IOHDAudioCodecDeviceUserClient readEDID] : 140 -> 136
~ -[IOHDAudioCodecDeviceUserClient getBDL:bdlEStructPtr:] : 224 -> 228
~ -[IOHDAudioCodecDeviceUserClient writeHighDefinitionAudioControllerRegisters] : 136 -> 132
~ -[IOHDAudioCodecDeviceUserClient transactVerbAndResponse:verb:payload:responsePtr:] : 180 -> 184
~ -[IOHDAudioCodecDeviceUserClient getCodecAddress:] : 156 -> 160
~ -[IOHDAudioCodecDeviceUserClient readHighDefinitionAudioControllerMaxBusStall:] : 208 -> 212
~ -[IOHDAudioCodecDeviceUserClient getHighDefinitionAudioControllerMaxBusStallEnable:] : 208 -> 212
~ -[IOHDAudioCodecDeviceUserClient getControllerVendorID:andProductID:] : 132 -> 124
~ -[IOHDAudioCodecDeviceUserClient getAppleHDADriver_loggingMessageMode] : 140 -> 144
~ -[IOHDAudioCodecDeviceUserClient setAppleHDADriver_loggingMessageMode:] : 132 -> 128
~ -[IOHDAudioCodecDeviceUserClient setAppleHDADriver_retaskMode:access:] : 140 -> 136
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/IOHDAudioCodecDeviceUserClient.m"
+ "Sound assertion \"0 != [self findFunctionNumber:false name:\"Dsp3ChOutput\" number:&funcNumber]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 470 goto Exit\n"
+ "Sound assertion \"0 != [self findFunctionNumber:false name:\"Dsp4ChOutput\" number:&funcNumber]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 480 goto Exit\n"
+ "Sound assertion \"0 != [self findFunctionNumber:false name:\"Dsp4ChOutput\" number:&funcNumber]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 529 goto Exit\n"
+ "Sound assertion \"0 != [self findFunctionNumber:false name:\"Dsp6ChOutput\" number:&funcNumber]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 540 goto Exit\n"
+ "Sound assertion \"0 != [self getFunctionName:nFunc :funcName :&size]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 657 goto Exit\n"
+ "Sound assertion \"0 != [self getParameter:funcNumber :kCh3Output_Parameter_Channel0MuteOP :ch1]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 523 goto Exit\n"
+ "Sound assertion \"0 != [self getParameter:funcNumber :kCh3Output_Parameter_Channel1MuteOP :ch2]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 524 goto Exit\n"
+ "Sound assertion \"0 != [self getParameter:funcNumber :kCh3Output_Parameter_Channel2MuteOP :ch3]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 525 goto Exit\n"
+ "Sound assertion \"0 != [self getParameter:funcNumber :kCh4Output_Parameter_Channel0MuteOP :ch1]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 532 goto Exit\n"
+ "Sound assertion \"0 != [self getParameter:funcNumber :kCh4Output_Parameter_Channel1MuteOP :ch2]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 533 goto Exit\n"
+ "Sound assertion \"0 != [self getParameter:funcNumber :kCh4Output_Parameter_Channel2MuteOP :ch3]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 534 goto Exit\n"
+ "Sound assertion \"0 != [self getParameter:funcNumber :kCh4Output_Parameter_Channel3MuteOP :ch4]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 535 goto Exit\n"
+ "Sound assertion \"0 != [self getParameter:funcNumber :kCh6Output_Parameter_Channel0MuteOP :ch1]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 543 goto Exit\n"
+ "Sound assertion \"0 != [self getParameter:funcNumber :kCh6Output_Parameter_Channel1MuteOP :ch2]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 544 goto Exit\n"
+ "Sound assertion \"0 != [self getParameter:funcNumber :kCh6Output_Parameter_Channel2MuteOP :ch3]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 545 goto Exit\n"
+ "Sound assertion \"0 != [self getParameter:funcNumber :kCh6Output_Parameter_Channel3MuteOP :ch4]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 546 goto Exit\n"
+ "Sound assertion \"0 != [self getParameter:funcNumber :kCh6Output_Parameter_Channel4MuteOP :ch5]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 547 goto Exit\n"
+ "Sound assertion \"0 != [self getParameter:funcNumber :kCh6Output_Parameter_Channel5MuteOP :ch6]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 548 goto Exit\n"
+ "Sound assertion \"0 != [self setParameter:funcNumber :kCh3Output_Parameter_Channel0MuteOP :ch1]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 473 goto Exit\n"
+ "Sound assertion \"0 != [self setParameter:funcNumber :kCh3Output_Parameter_Channel1MuteOP :ch2]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 474 goto Exit\n"
+ "Sound assertion \"0 != [self setParameter:funcNumber :kCh3Output_Parameter_Channel2MuteOP :ch3]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 475 goto Exit\n"
+ "Sound assertion \"0 != [self setParameter:funcNumber :kCh4Output_Parameter_Channel0MuteOP :ch1]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 484 goto Exit\n"
+ "Sound assertion \"0 != [self setParameter:funcNumber :kCh4Output_Parameter_Channel1MuteOP :ch2]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 485 goto Exit\n"
+ "Sound assertion \"0 != [self setParameter:funcNumber :kCh4Output_Parameter_Channel2MuteOP :ch3]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 486 goto Exit\n"
+ "Sound assertion \"0 != [self setParameter:funcNumber :kCh4Output_Parameter_Channel3MuteOP :ch4]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 487 goto Exit\n"
+ "Sound assertion \"0 != [self setParameter:funcNumber :kCh6Output_Parameter_Channel0MuteOP :ch1]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 496 goto Exit\n"
+ "Sound assertion \"0 != [self setParameter:funcNumber :kCh6Output_Parameter_Channel1MuteOP :ch2]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 497 goto Exit\n"
+ "Sound assertion \"0 != [self setParameter:funcNumber :kCh6Output_Parameter_Channel2MuteOP :ch3]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 498 goto Exit\n"
+ "Sound assertion \"0 != [self setParameter:funcNumber :kCh6Output_Parameter_Channel3MuteOP :ch4]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 499 goto Exit\n"
+ "Sound assertion \"0 != [self setParameter:funcNumber :kCh6Output_Parameter_Channel4MuteOP :ch5]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 500 goto Exit\n"
+ "Sound assertion \"0 != [self setParameter:funcNumber :kCh6Output_Parameter_Channel5MuteOP :ch6]\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 501 goto Exit\n"
+ "Sound assertion \"0 != result\" failed in \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 450 goto Exit\n"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/IOHDAudioCodecDeviceUserClient.m"
- "Sound assertion \"0 != [self findFunctionNumber:false name:\"Dsp3ChOutput\" number:&funcNumber]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 470 goto Exit\n"
- "Sound assertion \"0 != [self findFunctionNumber:false name:\"Dsp4ChOutput\" number:&funcNumber]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 480 goto Exit\n"
- "Sound assertion \"0 != [self findFunctionNumber:false name:\"Dsp4ChOutput\" number:&funcNumber]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 529 goto Exit\n"
- "Sound assertion \"0 != [self findFunctionNumber:false name:\"Dsp6ChOutput\" number:&funcNumber]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 540 goto Exit\n"
- "Sound assertion \"0 != [self getFunctionName:nFunc :funcName :&size]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 657 goto Exit\n"
- "Sound assertion \"0 != [self getParameter:funcNumber :kCh3Output_Parameter_Channel0MuteOP :ch1]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 523 goto Exit\n"
- "Sound assertion \"0 != [self getParameter:funcNumber :kCh3Output_Parameter_Channel1MuteOP :ch2]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 524 goto Exit\n"
- "Sound assertion \"0 != [self getParameter:funcNumber :kCh3Output_Parameter_Channel2MuteOP :ch3]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 525 goto Exit\n"
- "Sound assertion \"0 != [self getParameter:funcNumber :kCh4Output_Parameter_Channel0MuteOP :ch1]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 532 goto Exit\n"
- "Sound assertion \"0 != [self getParameter:funcNumber :kCh4Output_Parameter_Channel1MuteOP :ch2]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 533 goto Exit\n"
- "Sound assertion \"0 != [self getParameter:funcNumber :kCh4Output_Parameter_Channel2MuteOP :ch3]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 534 goto Exit\n"
- "Sound assertion \"0 != [self getParameter:funcNumber :kCh4Output_Parameter_Channel3MuteOP :ch4]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 535 goto Exit\n"
- "Sound assertion \"0 != [self getParameter:funcNumber :kCh6Output_Parameter_Channel0MuteOP :ch1]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 543 goto Exit\n"
- "Sound assertion \"0 != [self getParameter:funcNumber :kCh6Output_Parameter_Channel1MuteOP :ch2]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 544 goto Exit\n"
- "Sound assertion \"0 != [self getParameter:funcNumber :kCh6Output_Parameter_Channel2MuteOP :ch3]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 545 goto Exit\n"
- "Sound assertion \"0 != [self getParameter:funcNumber :kCh6Output_Parameter_Channel3MuteOP :ch4]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 546 goto Exit\n"
- "Sound assertion \"0 != [self getParameter:funcNumber :kCh6Output_Parameter_Channel4MuteOP :ch5]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 547 goto Exit\n"
- "Sound assertion \"0 != [self getParameter:funcNumber :kCh6Output_Parameter_Channel5MuteOP :ch6]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 548 goto Exit\n"
- "Sound assertion \"0 != [self setParameter:funcNumber :kCh3Output_Parameter_Channel0MuteOP :ch1]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 473 goto Exit\n"
- "Sound assertion \"0 != [self setParameter:funcNumber :kCh3Output_Parameter_Channel1MuteOP :ch2]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 474 goto Exit\n"
- "Sound assertion \"0 != [self setParameter:funcNumber :kCh3Output_Parameter_Channel2MuteOP :ch3]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 475 goto Exit\n"
- "Sound assertion \"0 != [self setParameter:funcNumber :kCh4Output_Parameter_Channel0MuteOP :ch1]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 484 goto Exit\n"
- "Sound assertion \"0 != [self setParameter:funcNumber :kCh4Output_Parameter_Channel1MuteOP :ch2]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 485 goto Exit\n"
- "Sound assertion \"0 != [self setParameter:funcNumber :kCh4Output_Parameter_Channel2MuteOP :ch3]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 486 goto Exit\n"
- "Sound assertion \"0 != [self setParameter:funcNumber :kCh4Output_Parameter_Channel3MuteOP :ch4]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 487 goto Exit\n"
- "Sound assertion \"0 != [self setParameter:funcNumber :kCh6Output_Parameter_Channel0MuteOP :ch1]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 496 goto Exit\n"
- "Sound assertion \"0 != [self setParameter:funcNumber :kCh6Output_Parameter_Channel1MuteOP :ch2]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 497 goto Exit\n"
- "Sound assertion \"0 != [self setParameter:funcNumber :kCh6Output_Parameter_Channel2MuteOP :ch3]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 498 goto Exit\n"
- "Sound assertion \"0 != [self setParameter:funcNumber :kCh6Output_Parameter_Channel3MuteOP :ch4]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 499 goto Exit\n"
- "Sound assertion \"0 != [self setParameter:funcNumber :kCh6Output_Parameter_Channel4MuteOP :ch5]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 500 goto Exit\n"
- "Sound assertion \"0 != [self setParameter:funcNumber :kCh6Output_Parameter_Channel5MuteOP :ch6]\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 501 goto Exit\n"
- "Sound assertion \"0 != result\" failed in \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleHDA_frameworks/HDAFramework/HDADSPInterface.mm\" at line 450 goto Exit\n"

```
