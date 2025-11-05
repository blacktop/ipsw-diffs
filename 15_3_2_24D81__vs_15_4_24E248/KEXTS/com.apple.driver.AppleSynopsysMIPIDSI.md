## com.apple.driver.AppleSynopsysMIPIDSI

> `com.apple.driver.AppleSynopsysMIPIDSI`

```diff

 96.0.0.0.0
   __TEXT.__const: 0x10
   __TEXT.__cstring: 0x26ea
-  __TEXT_EXEC.__text: 0x92b8
+  __TEXT_EXEC.__text: 0x9530
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xb0

   __DATA_CONST.__const: 0x1180
   __DATA_CONST.__kalloc_type: 0x100
   __DATA_CONST.__kalloc_var: 0x550
-  UUID: 9B880BAB-474D-3108-9CEF-FDEF47E67EB1
+  UUID: 9FB52710-09B9-3603-AEA6-CCA1BDA60AFB
   Functions: 236
   Symbols:   630
   CStrings:  150
Functions:
~ __ZN30AppleSynopsysMIPIDSIController5startEP9IOService : 7708 -> 7932
~ __ZN30AppleSynopsysMIPIDSIController11_enterTraceEjj : 156 -> 168
~ __ZN30AppleSynopsysMIPIDSIController11_enableDSIMEb : 580 -> 616
~ __ZN30AppleSynopsysMIPIDSIController20enableInterfaceGatedEb : 2356 -> 2396
~ __ZN30AppleSynopsysMIPIDSIController24enableHighSpeedModeGatedEb : 612 -> 604
~ __ZN30AppleSynopsysMIPIDSIController16enableVideoGatedEb : 400 -> 396
~ __ZN30AppleSynopsysMIPIDSIController21sendShortCommandGatedEhhh : 344 -> 352
~ __ZN30AppleSynopsysMIPIDSIController20sendLongCommandGatedEhPKhy : 648 -> 660
~ __ZN30AppleSynopsysMIPIDSIController24receiveShortCommandGatedEhPh : 628 -> 664
~ __ZN30AppleSynopsysMIPIDSIController23receiveLongCommandGatedEhPhPy : 956 -> 992
~ __ZN30AppleSynopsysMIPIDSIController17setLPMEnableGatedEb : 268 -> 280
~ __ZN30AppleSynopsysMIPIDSIController18_programFrameGatedEPj : 112 -> 124
~ __ZN30AppleSynopsysMIPIDSIController17_isFrameDoneGatedEb : 124 -> 132
~ __ZN30AppleSynopsysMIPIDSIController16_isReadDoneGatedEv : 152 -> 160
~ __ZN30AppleSynopsysMIPIDSIController17_isDMMExitedGatedEv : 280 -> 296
~ __ZN30AppleSynopsysMIPIDSIController18_isCommitDoneGatedEv : 280 -> 296
~ __ZN30AppleSynopsysMIPIDSIController24_calculateRegisterValuesEPjS0_P16display_timing_tP10mipi_lpm_t : 752 -> 756
~ __ZN30AppleSynopsysMIPIDSIController24_sacConvertFrequencyListEPjP18dsimSACAggressor_t : 224 -> 236
~ __ZN30AppleSynopsysMIPIDSIController25_sacGenerateFrequencyListEv : 1512 -> 1560
~ __ZN30AppleSynopsysMIPIDSIController10_sacActionEj : 104 -> 108
~ __ZN30AppleSynopsysMIPIDSIController18_sacChangePLLGatedE23dsimSACAggressorIndex_tj : 164 -> 200
~ __ZN30AppleSynopsysMIPIDSIController18_sacWaitPLLRequestEP23dsimSACAggressorIndex_tPj : 288 -> 300
~ __ZN30AppleSynopsysMIPIDSIController13_sacLPMActionEj : 104 -> 108
~ __ZN30AppleSynopsysMIPIDSIController10_sacThreadEv : 916 -> 964
~ __ZN30AppleSynopsysMIPIDSIController14_sacSadTimeoutEP18IOTimerEventSource : 160 -> 152
~ __ZN30AppleSynopsysMIPIDSIController24_sacSadExtremeFreqSwitchEP18IOTimerEventSource : 156 -> 148
~ __ZN30AppleSynopsysMIPIDSIController20callPlatformFunctionEPK8OSSymbolbPvS3_S3_S3_ : 844 -> 848
~ __ZN30AppleSynopsysMIPIDSIController8_pollRegEjjjb : 336 -> 344
~ __ZN30AppleSynopsysMIPIDSIController14_changeModeCfgEj : 160 -> 164
~ __ZN30AppleSynopsysMIPIDSIController22_unlockMIPITransactionEv : 68 -> 64
~ __ZN30AppleSynopsysMIPIDSIController25sendSWMPRLongCommandGatedEhPKhy : 436 -> 440
~ __ZN30AppleSynopsysMIPIDSIController16getDisplayTimingEbP16display_timing_t : 92 -> 96
~ __ZN30AppleSynopsysMIPIDSIController27_sacEnablePLLGatedWithGraceEb : 164 -> 160
~ __ZN30AppleSynopsysMIPIDSIController27_sacEnablePLLGatedClockStopEb : 220 -> 224
~ __ZN30AppleSynopsysMIPIDSIController29_sacEnablePLLGatedWithMIPIPLLEb : 252 -> 256
~ __ZN30AppleSynopsysMIPIDSIController35_sacEnablePLLGatedWithMIPIPLLSimpleEb : 220 -> 212
~ _ZN30AppleSynopsysMIPIDSIController5startEP9IOService.cold.1 : 56 -> 100
~ _ZN30AppleSynopsysMIPIDSIController5startEP9IOService.cold.3 : 44 -> 56
~ _ZN30AppleSynopsysMIPIDSIController5startEP9IOService.cold.4 : 44 -> 56
~ _ZN30AppleSynopsysMIPIDSIController5startEP9IOService.cold.5 : 44 -> 56
~ _ZN30AppleSynopsysMIPIDSIController5startEP9IOService.cold.6 : 44 -> 56
~ _ZN30AppleSynopsysMIPIDSIController5startEP9IOService.cold.9 : 56 -> 44
~ _ZN30AppleSynopsysMIPIDSIController5startEP9IOService.cold.10 : 56 -> 44
~ _ZN30AppleSynopsysMIPIDSIController5startEP9IOService.cold.12 : 56 -> 44
~ _ZN30AppleSynopsysMIPIDSIController5startEP9IOService.cold.13 : 56 -> 44
~ _ZN30AppleSynopsysMIPIDSIController5startEP9IOService.cold.15 : 100 -> 56
~ _ZN30AppleSynopsysMIPIDSIController20enableInterfaceGatedEb.cold.1 : 64 -> 56
~ _ZN30AppleSynopsysMIPIDSIController20enableInterfaceGatedEb.cold.2 : 56 -> 64
~ _ZN30AppleSynopsysMIPIDSIController21sendShortCommandGatedEhhh.cold.2 : 60 -> 56
~ _ZN30AppleSynopsysMIPIDSIController21sendShortCommandGatedEhhh.cold.3 : 56 -> 60
~ _ZN30AppleSynopsysMIPIDSIController20sendLongCommandGatedEhPKhy.cold.2 : 60 -> 56
~ _ZN30AppleSynopsysMIPIDSIController20sendLongCommandGatedEhPKhy.cold.3 : 56 -> 60
~ _ZN30AppleSynopsysMIPIDSIController24receiveShortCommandGatedEhPh.cold.2 : 60 -> 56
~ _ZN30AppleSynopsysMIPIDSIController24receiveShortCommandGatedEhPh.cold.3 : 56 -> 60
~ _ZN30AppleSynopsysMIPIDSIController23receiveLongCommandGatedEhPhPy.cold.2 : 60 -> 56
~ _ZN30AppleSynopsysMIPIDSIController23receiveLongCommandGatedEhPhPy.cold.3 : 56 -> 60
~ _ZN30AppleSynopsysMIPIDSIController17_enableSWMPRGatedEb.cold.3 : 44 -> 56
~ _ZN30AppleSynopsysMIPIDSIController17_enableSWMPRGatedEb.cold.5 : 56 -> 44
~ _ZN30AppleSynopsysMIPIDSIController17_isDMMExitedGatedEv.cold.2 : 60 -> 56
~ _ZN30AppleSynopsysMIPIDSIController17_isDMMExitedGatedEv.cold.3 : 56 -> 60
~ _ZN30AppleSynopsysMIPIDSIController18_isCommitDoneGatedEv.cold.2 : 60 -> 56
~ _ZN30AppleSynopsysMIPIDSIController18_isCommitDoneGatedEv.cold.3 : 56 -> 60
~ _ZN30AppleSynopsysMIPIDSIController25_sacGenerateFrequencyListEv.cold.1 : 44 -> 52
~ _ZN30AppleSynopsysMIPIDSIController25_sacGenerateFrequencyListEv.cold.4 : 52 -> 44
~ _ZN30AppleSynopsysMIPIDSIController26sendSWMPRShortCommandGatedEhhh.cold.4 : 60 -> 56
~ _ZN30AppleSynopsysMIPIDSIController26sendSWMPRShortCommandGatedEhhh.cold.5 : 56 -> 60

```
