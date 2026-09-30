## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2055.59.1.0.0
-  __TEXT.__text: 0x6b5518
-  __TEXT.__auth_stubs: 0x4fb0
-  __TEXT.__objc_methlist: 0x2d868
-  __TEXT.__const: 0x7d90
-  __TEXT.__cstring: 0x7f279
-  __TEXT.__oslogstring: 0xec25b
-  __TEXT.__gcc_except_tab: 0x2508
+2055.64.1.1.2
+  __TEXT.__text: 0x6b6930
+  __TEXT.__auth_stubs: 0x4fc0
+  __TEXT.__objc_methlist: 0x2d8d8
+  __TEXT.__const: 0x7dd0
+  __TEXT.__cstring: 0x7f5d4
+  __TEXT.__oslogstring: 0xec3b1
+  __TEXT.__gcc_except_tab: 0x253c
   __TEXT.__ustring: 0x144
-  __TEXT.__unwind_info: 0xd0f0
+  __TEXT.__unwind_info: 0xd130
   __TEXT.__objc_classname: 0x4777
-  __TEXT.__objc_methname: 0x716e2
-  __TEXT.__objc_methtype: 0x24546
-  __TEXT.__objc_stubs: 0x47a80
-  __DATA_CONST.__got: 0x18d0
-  __DATA_CONST.__const: 0x60a0
+  __TEXT.__objc_methname: 0x71867
+  __TEXT.__objc_methtype: 0x2455f
+  __TEXT.__objc_stubs: 0x47ba0
+  __DATA_CONST.__got: 0x18d8
+  __DATA_CONST.__const: 0x6128
   __DATA_CONST.__objc_classlist: 0x1178
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x438
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14830
+  __DATA_CONST.__objc_selrefs: 0x14878
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0xfa0
   __DATA_CONST.__objc_arraydata: 0x2070
-  __AUTH_CONST.__auth_got: 0x27f0
+  __AUTH_CONST.__auth_got: 0x27f8
   __AUTH_CONST.__auth_ptr: 0xc8
   __AUTH_CONST.__const: 0x3370
-  __AUTH_CONST.__cfstring: 0x22560
-  __AUTH_CONST.__objc_const: 0x610a0
+  __AUTH_CONST.__cfstring: 0x22580
+  __AUTH_CONST.__objc_const: 0x611c0
   __AUTH_CONST.__objc_intobj: 0x4560
   __AUTH_CONST.__objc_arrayobj: 0x1710
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x160
   __AUTH_CONST.__objc_dictobj: 0x2d0
-  __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x6338
-  __DATA.__data: 0x73c8
-  __DATA.__bss: 0xb98
+  __DATA.__objc_ivar: 0x6350
+  __DATA.__data: 0x7430
+  __DATA.__bss: 0xb60
   __DATA.__common: 0x55
-  __DATA_DIRTY.__objc_data: 0xabe0
+  __DATA_DIRTY.__objc_data: 0xaeb0
   __DATA_DIRTY.__data: 0x180
-  __DATA_DIRTY.__bss: 0x360
+  __DATA_DIRTY.__bss: 0x390
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/PrivateFrameworks/FTServices.framework/FTServices
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
+  - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/PrivacyAccounting.framework/PrivacyAccounting
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationFeed.framework/SymptomPresentationFeed

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 27715
-  Symbols:   32425
-  CStrings:  47119
+  Functions: 27738
+  Symbols:   32450
+  CStrings:  47155
 
Symbols:
+ _OBJC_CLASS_$_OSASystemConfiguration
+ _timingsafe_bcmp
CStrings:
+ " [%!s(MISSING)] %!s(MISSING):%!d(MISSING) Attempt to send un-encrypted packet with rtpHandle=%!p(MISSING), VCMediaQueue=%!p(MISSING), cipherSuite=%!d(MISSING), and ssrc=%!u(MISSING)"
+ " [%!s(MISSING)] %!s(MISSING):%!d(MISSING) Failed to create reporting event dictionary"
+ " [%!s(MISSING)] %!s(MISSING):%!d(MISSING) Falling back to VCMediaStreamCipherSuiteCipherAES128AuthNoneRCCM3 for streamGroupID=%!s(MISSING)"
+ " [%!s(MISSING)] %!s(MISSING):%!d(MISSING) Negotiating cipherSuite=%!s(MISSING) [%!l(MISSING)d] for streamGroupID=%!s(MISSING)"
+ " [%!s(MISSING)] %!s(MISSING):%!d(MISSING) [AR_RX] AspectRatio fromVisibleRect=%!f(MISSING), fromContentRect=%!f(MISSING)"
+ " [%!s(MISSING)] %!s(MISSING):%!d(MISSING) [AR_RX] frameWidth=%!d(MISSING), frameHeight=%!d(MISSING)"
+ " [%!s(MISSING)] %!s(MISSING):%!d(MISSING) deviceStateMessage is nil"
+ "+[VCMediaNegotiatorStreamGroupU1Configuration negotiateU1CipherSuiteForStreamGroupID:remoteSupportedCipherSuites:]"
+ "-[VCAudioStream setupCaptionsCoordinatorsWithFormat:direction:]"
+ "-[VCSession sendDeviceStateMessageToParticipant:withStatus:]"
+ "-[VCSession(Messaging) handleDeviceStateMessage:forParticipantId:]"
+ "-[VCVideoCaptureServer setLocalVideoDestination:]_block_invoke"
+ "-[VCVideoStreamReceiver reportVideoStallStatus:]"
+ "2055.64.1.1.2"
+ "@24@0:8^{tagSRTPINFO=ii{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}IISSIIQii[32C][14C][32C][14C][32C]{_opaque_pthread_mutex_t=q[56c]}^v^vII{os_unfair_lock_s=I}{tagSRTPCryptContext=^{_CCCryptor}}{tagSRTPTransformPolicy=iiiiiiiiI}IB}16"
+ "TC,N,V_supportedDirection"
+ "T^{tagSRTPINFO=ii{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}IISSIIQii[32C][14C][32C][14C][32C]{_opaque_pthread_mutex_t=q[56c]}^v^vII{os_unfair_lock_s=I}{tagSRTPCryptContext=^{_CCCryptor}}{tagSRTPTransformPolicy=iiiiiiiiI}IB},R"
+ "VCMediaStreamCipherSuiteCipherAES128AuthNone"
+ "VCMediaStreamCipherSuiteCipherAES128AuthNoneRCCM3"
+ "VCMediaStreamCipherSuiteCipherAES128AuthSHA180"
+ "VCMediaStreamCipherSuiteCipherAES128AuthSHA232RCCM2Deferred"
+ "VCMediaStreamCipherSuiteCipherAES128AuthSHA280RCCM2Deferred"
+ "VCMediaStreamCipherSuiteCipherAES256AuthNone"
+ "VCMediaStreamCipherSuiteCipherAES256AuthNoneRCCM3"
+ "VCMediaStreamCipherSuiteCipherAES256AuthSHA180"
+ "VCMediaStreamCipherSuiteCipherNoneAuthNone"
+ "VCMediaStreamCipherSuiteCipherNoneAuthSHA180"
+ "VCRC [%!s(MISSING)] %!s(MISSING):%!d(MISSING) [%!p(MISSING)] _txLinkType changed to=%!d(MISSING) ecnLinkType=%!d(MISSING) with isECNEnabled=%!d(MISSING), isECNLinkType=%!d(MISSING)"
+ "VCSession [%!s(MISSING)] %!s(MISSING):%!d(MISSING) Diagnostics collection is off"
+ "VCSessionMessageTopicDeviceState"
+ "VCVideoCaptureServer [%!s(MISSING)] %!s(MISSING):%!d(MISSING) _defaultLandscapeAspectRatio=%!@(MISSING)"
+ "VCVideoCaptureServer [%!s(MISSING)] %!s(MISSING):%!d(MISSING) _defaultPortraitAspectRatio=%!@(MISSING)"
+ "^{tagSRTPINFO=ii{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}IISSIIQii[32C][14C][32C][14C][32C]{_opaque_pthread_mutex_t=q[56c]}^v^vII{os_unfair_lock_s=I}{tagSRTPCryptContext=^{_CCCryptor}}{tagSRTPTransformPolicy=iiiiiiiiI}IB}16@0:8"
+ "_isDNUCollectionEnabled"
+ "_lastFeedbackTargetBitrate"
+ "_lastFeedbackTime"
+ "_lastThermalLevel"
+ "_localRCEventTime"
+ "_supportedDirection"
+ "captureFormatPrefer16by9ForSquare"
+ "cleanUpEventQueue"
+ "handleDeviceStateMessage:forParticipantId:"
+ "optInApple"
+ "reportVideoStallStatus:"
+ "restartPreview"
+ "sendDeviceStateMessageToParticipant:withStatus:"
+ "setSupportedDirection:"
+ "setUpNegotiatedSystemAudioResultsWithRemoteMediaBlob:"
+ "setupCaptionsCoordinatorsWithFormat:direction:"
+ "setupDeviceStateMessage"
+ "supportedDirection"
+ "v24@0:8^{tagSRTPINFO=ii{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}IISSIIQii[32C][14C][32C][14C][32C]{_opaque_pthread_mutex_t=q[56c]}^v^vII{os_unfair_lock_s=I}{tagSRTPCryptContext=^{_CCCryptor}}{tagSRTPTransformPolicy=iiiiiiiiI}IB}16"
+ "v32@0:8^{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}16q24"
+ "{tagSRTPINFO=\"fSRTPInitialized\"i\"fCancelled\"i\"xWait\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}\"cWait\"{_opaque_pthread_cond_t=\"__sig\"q\"__opaque\"[40c]}\"dwSSRC\"I\"dwRTPROC\"I\"wFirstRTPSeq\"S\"wHighestRTPSeq\"S\"dwFirstRTCPSeq\"I\"dwHighestRTCPSeq\"I\"SRTPIndex\"Q\"mediaKeyLength\"i\"sessionKeyLength\"i\"MediaKey\"[32C]\"MasterSalt\"[14C]\"SessionKey\"[32C]\"SessionSalt\"[14C]\"SessionAuthenticationKey\"[32C]\"MKIAccess\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}\"mediaKeyIndex\"^v\"mediaKeyIndexInPacket\"^v\"SRTCPIndex\"I\"dwDerivationRate\"I\"cryptContextLock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"cryptContext\"{tagSRTPCryptContext=\"ccCryptorRef\"^{_CCCryptor}}\"policy\"{tagSRTPTransformPolicy=\"cipherMode\"i\"mediaKeyLength\"i\"sessionKeyLength\"i\"sessionSaltLength\"i\"authenticationMode\"i\"sessionAuthenticationKeyLength\"i\"sessionAuthenticationTagLength\"i\"cipherSuite\"i\"maxTagBufferSize\"I}\"operatingMode\"I\"enableEncryptionDebug\"B}"
- " [%!s(MISSING)] %!s(MISSING):%!d(MISSING) Attempt to send un-encrypted packet with rtpHandle=%!p(MISSING), VCMediaQueue=%!p(MISSING), cipherSuite=%!d(MISSING), and ssrc=%!d(MISSING)"
- " [%!s(MISSING)] %!s(MISSING):%!d(MISSING) OneToOne mode supported %!d(MISSING)"
- " [%!s(MISSING)] %!s(MISSING):%!d(MISSING) [AR_RX] AspectRatio fromVisibleRect=%!f(MISSING), fromContextRect=%!f(MISSING)"
- "-[VCAudioStream setupCaptionsCoordinatorsWithFormat:]"
- "-[VCDefaults supportsOneToOneMode]"
- "2055.59.1"
- "@24@0:8^{tagSRTPINFO=ii{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}IISSIIQii[32C][14C][32C][14C][32C]{_opaque_pthread_mutex_t=q[56c]}^v^vII{os_unfair_lock_s=I}{tagSRTPCryptContext=^{_CCCryptor}}{tagSRTPTransformPolicy=iiiiiiii}IB}16"
- "T^{tagSRTPINFO=ii{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}IISSIIQii[32C][14C][32C][14C][32C]{_opaque_pthread_mutex_t=q[56c]}^v^vII{os_unfair_lock_s=I}{tagSRTPCryptContext=^{_CCCryptor}}{tagSRTPTransformPolicy=iiiiiiii}IB},R"
- "VCRC [%!s(MISSING)] %!s(MISSING):%!d(MISSING) [%!p(MISSING)] _txLinkType changed to=%!d(MISSING) with isECNEnabled=%!d(MISSING)"
- "VCVideoCaptureServer [%!s(MISSING)] %!s(MISSING):%!d(MISSING) _defaultLandscapeAspectRatio=(%!f(MISSING), %!f(MISSING))"
- "VCVideoCaptureServer [%!s(MISSING)] %!s(MISSING):%!d(MISSING) _defaultPortraitAspectRatio=(%!f(MISSING), %!f(MISSING))"
- "^{tagSRTPINFO=ii{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}IISSIIQii[32C][14C][32C][14C][32C]{_opaque_pthread_mutex_t=q[56c]}^v^vII{os_unfair_lock_s=I}{tagSRTPCryptContext=^{_CCCryptor}}{tagSRTPTransformPolicy=iiiiiiii}IB}16@0:8"
- "isInitiatorForRemoteParticipant:"
- "setupCaptionsCoordinatorsWithFormat:"
- "setupNegotiatedSystemAudioResultsWithLocalConfigOnly"
- "v24@0:8^{tagSRTPINFO=ii{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}IISSIIQii[32C][14C][32C][14C][32C]{_opaque_pthread_mutex_t=q[56c]}^v^vII{os_unfair_lock_s=I}{tagSRTPCryptContext=^{_CCCryptor}}{tagSRTPTransformPolicy=iiiiiiii}IB}16"
- "v24@0:8^{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}16"
- "{tagSRTPINFO=\"fSRTPInitialized\"i\"fCancelled\"i\"xWait\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}\"cWait\"{_opaque_pthread_cond_t=\"__sig\"q\"__opaque\"[40c]}\"dwSSRC\"I\"dwRTPROC\"I\"wFirstRTPSeq\"S\"wHighestRTPSeq\"S\"dwFirstRTCPSeq\"I\"dwHighestRTCPSeq\"I\"SRTPIndex\"Q\"mediaKeyLength\"i\"sessionKeyLength\"i\"MediaKey\"[32C]\"MasterSalt\"[14C]\"SessionKey\"[32C]\"SessionSalt\"[14C]\"SessionAuthenticationKey\"[32C]\"MKIAccess\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}\"mediaKeyIndex\"^v\"mediaKeyIndexInPacket\"^v\"SRTCPIndex\"I\"dwDerivationRate\"I\"cryptContextLock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"cryptContext\"{tagSRTPCryptContext=\"ccCryptorRef\"^{_CCCryptor}}\"policy\"{tagSRTPTransformPolicy=\"cipherMode\"i\"mediaKeyLength\"i\"sessionKeyLength\"i\"sessionSaltLength\"i\"authenticationMode\"i\"sessionAuthenticationKeyLength\"i\"sessionAuthenticationTagLength\"i\"cipherSuite\"i}\"operatingMode\"I\"enableEncryptionDebug\"B}"

```
