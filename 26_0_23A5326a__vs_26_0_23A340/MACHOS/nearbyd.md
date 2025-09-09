## nearbyd

> `/usr/libexec/nearbyd`

```diff

 505.0.13.0.0
-  __TEXT.__text: 0x4b5d9c
+  __TEXT.__text: 0x4b8464
   __TEXT.__auth_stubs: 0x2960
-  __TEXT.__objc_stubs: 0x13080
+  __TEXT.__objc_stubs: 0x131c0
   __TEXT.__init_offsets: 0x6c4
-  __TEXT.__objc_methlist: 0xd2a4
-  __TEXT.__gcc_except_tab: 0x515bc
-  __TEXT.__const: 0x353f80
-  __TEXT.__cstring: 0x35802
-  __TEXT.__objc_methname: 0x1d54b
-  __TEXT.__oslogstring: 0x56abe
+  __TEXT.__objc_methlist: 0xd314
+  __TEXT.__gcc_except_tab: 0x519dc
+  __TEXT.__const: 0x353fa0
+  __TEXT.__cstring: 0x35a62
+  __TEXT.__objc_methname: 0x1d718
+  __TEXT.__oslogstring: 0x56f6e
   __TEXT.__objc_classname: 0x1a8e
-  __TEXT.__objc_methtype: 0x1e0b0
+  __TEXT.__objc_methtype: 0x1e3b6
   __TEXT.__swift5_typeref: 0x9b
   __TEXT.__swift5_capture: 0x20
   __TEXT.__constg_swiftt: 0x9c
   __TEXT.__swift5_reflstr: 0x1a
   __TEXT.__swift5_fieldmd: 0x34
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x19c68
+  __TEXT.__unwind_info: 0x19ce8
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x14c8
-  __DATA_CONST.__got: 0xa10
+  __DATA_CONST.__got: 0xa90
   __DATA_CONST.__auth_ptr: 0xc0
-  __DATA_CONST.__const: 0x22e88
-  __DATA_CONST.__cfstring: 0x14cc0
+  __DATA_CONST.__const: 0x22e98
+  __DATA_CONST.__cfstring: 0x14dc0
   __DATA_CONST.__objc_classlist: 0x528
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x260

   __DATA_CONST.__objc_arrayobj: 0x1e0
   __DATA_CONST.__objc_intobj: 0x678
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x16830
-  __DATA.__objc_selrefs: 0x5ce8
-  __DATA.__objc_ivar: 0x15f8
+  __DATA.__objc_const: 0x168b0
+  __DATA.__objc_selrefs: 0x5d38
+  __DATA.__objc_ivar: 0x1608
   __DATA.__objc_data: 0x3460
   __DATA.__data: 0x312c
-  __DATA.__bss: 0xd1b8
+  __DATA.__bss: 0xd1d8
   __DATA.__common: 0xd18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FA5E1D24-77FD-3956-A7CB-B0513C62EAAB
-  Functions: 20608
-  Symbols:   1013
-  CStrings:  21049
+  UUID: 2C4D2F61-85BF-36EF-BEF1-EA88CB4EC5D5
+  Functions: 20623
+  Symbols:   1029
+  CStrings:  21114
 
Symbols:
+ _CLDurianNBRangingAcqDitherMaxKey
+ _CLDurianNBRangingAcqRetryIntervalKey
+ _CLDurianNBRangingAcqTimeoutKey
+ _CLDurianNBRangingDebugFlagsKey
+ _CLDurianNBRangingIntervalKey
+ _CLDurianNBRangingMMSFragCountryCodeKey
+ _CLDurianNBRangingMMSGapKey
+ _CLDurianNBRangingMMSPSRKey
+ _CLDurianNBRangingMMSSequenceIdxKey
+ _CLDurianNBRangingMMSSlotSizeKey
+ _CLDurianNBRangingNBChannelSelectMaskKey
+ _CLDurianNBRangingNBCountryCodesKey
+ _CLDurianNBRangingNBMaskNapChannelKey
+ _CLDurianNBRangingRangingTimeoutKey
+ _CLDurianNBRangingSarCountryCodesKey
+ _CLDurianNBRangingVersionKey
CStrings:
+ "#ses-item-loc,Dithered duty cycled acquisition not valid for responder"
+ "#ses-item-loc,Extended_Precision_Finding_Core_Tech enabled"
+ "#ses-item-loc,Failed to allocate an NBAMMS session. Error: %s"
+ "#ses-item-loc,ItemSupportsEDM defaults set to %s"
+ "#ses-item-loc,MixedMMS selected for ranging: %s"
+ "#ses-item-loc,NBPreambleRandomizationForItemFinding defaults set to %s"
+ "#ses-item-loc,NBTimeDitheringForItemFinding defaults set to %s"
+ "#ses-item-loc,NIItemLocalizer NBAMMS session: invalidate"
+ "#ses-item-loc,No NBA-MMS slots are available - switching to FC1-ND ranging mode"
+ "#ses-item-loc,PRRangingManager prepareNBAMMSServiceRequest #companion-retry"
+ "#ses-item-loc,Provided duty cycle leads to scan window > scheduling interval - (start time offset + interface delays), using entire available scan window"
+ "#ses-item-loc,RangeConfigNBAMMS dict: %@"
+ "#ses-item-loc,UseMixedMMSForItemFinding defaults set to %s"
+ "#ses-item-loc,Using NAP channel %d from defaults writes"
+ "#ses-item-loc,[CL] configureNBRangingOnDevice"
+ "#ses-item-loc,[CL] startNBRangingOnDevice with irk: %@"
+ "#ses-item-loc,_useTimeDitheringForNBARanging set to %s, _usePreambleRandomizationForNBARanging set to %s"
+ "#ses-item-loc,regulatory and sar groups not available"
+ "-[NIServerItemLocalizerSession _prepareNBAMMSServiceRequest]"
+ "-[NIServerItemLocalizerSession _updateNBAMMSCompanionConfigurationCommandWithRequest:rangeConfig:]"
+ "-[NIServerItemLocalizerSession run]"
+ "/AppleInternal/Library/BuildRoots/4~B8cwugBoUN9zp8QrRNB-oHjwWfb4gW3-pT7bW-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/4~B8cwugBoUN9zp8QrRNB-oHjwWfb4gW3-pT7bW-Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
+ "@24@0:8^{RangeConfigNBAMMS=CCCCCCCCSSCCCCSC}16"
+ "AirPods3,4"
+ "B32@0:8r^v16^{RangeConfigNBAMMS=CCCCCCCCSSCCCCSC}24"
+ "Device1,22034"
+ "Device1,8232"
+ "Device1,8233"
+ "Device1,8239"
+ "Extended_Precision_Finding_Core_Tech"
+ "FindAirPodsCase_R2"
+ "FindAirTag_R2"
+ "IRK != nil"
+ "ItemSupportsEDM"
+ "NBAMMS"
+ "NBPreambleRandomizationForItemFinding"
+ "NBTimeDitheringForItemFinding"
+ "Unable to init NBAMMS session"
+ "UseMixedMMSForItemFinding"
+ "[12B]"
+ "_getDictFromRangeConfigNBAMMS:"
+ "_getDitherConst:"
+ "_noAvailableSlotForNBARanging"
+ "_pickRandomNbUwbAcquisitionChannelWithUUID:"
+ "_populateNBAMMSRoseStartRangingOptions:"
+ "_prepareNBAMMSServiceRequest"
+ "_roseServiceRequest.has_value()"
+ "_selectNBAMMSMode"
+ "_updateNBAMMSCompanionConfigurationCommandWithRequest:rangeConfig:"
+ "_useMixedMMSForNBARanging"
+ "_usePreambleRandomizationForNBARanging"
+ "_useTimeDitheringForNBARanging"
+ "configureNBRangingOnDevice:withParams:"
+ "macAddressForIRK:"
+ "proxima"
+ "request.range_enable_params.nbamms.nb_bch.has_value()"
+ "startNBRangingOnDevice:withIRK:"
+ "{RoseStartRangingOptions={optional<rose::RoseDeviceDescriptor>=(?=c{RoseDeviceDescriptor=i{optional<std::array<unsigned char, 16>>=(?=c{array<unsigned char, 16UL>=[16C]})B}{optional<std::array<unsigned char, 8>>=(?=c{array<unsigned char, 8UL>=[8C]})B}{optional<std::array<unsigned char, 6>>=(?=c{array<unsigned char, 6UL>=[6C]})B}})B}QCIIf{optional<rose::ConnectionEventTriggerDescriptor>=(?=c{ConnectionEventTriggerDescriptor=I})B}{optional<unsigned char>=(?=cC)B}{optional<unsigned short>=(?=cS)B}{optional<unsigned char>=(?=cC)B}{optional<unsigned int>=(?=cI)B}{optional<unsigned int>=(?=cI)B}{optional<float>=(?=cf)B}}20@0:8B16"
+ "{optional<unsigned char>=(?=cC)B}20@0:8B16"
- "/AppleInternal/Library/BuildRoots/4~B7lSugAlsQhic2lYCaICUst6Dfxm0PFDrzwQ-7k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/4~B7lSugAlsQhic2lYCaICUst6Dfxm0PFDrzwQ-7k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
- "[10B]"

```
