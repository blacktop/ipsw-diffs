## AirPlayReceiver

> `/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver`

```diff

-1005.12.1.0.0
-  __TEXT.__text: 0x1791e0
+1005.13.1.1.0
+  __TEXT.__text: 0x1799cc
   __TEXT.__objc_methlist: 0xaec
   __TEXT.__const: 0x2762b
   __TEXT.__dlopen_cstrs: 0xad
-  __TEXT.__gcc_except_tab: 0x838
-  __TEXT.__cstring: 0x332b3
+  __TEXT.__gcc_except_tab: 0x890
+  __TEXT.__cstring: 0x33395
   __TEXT.__oslogstring: 0x2eb
-  __TEXT.__unwind_info: 0x1c80
+  __TEXT.__unwind_info: 0x1cc8
   __TEXT.__eh_frame: 0x128
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x998
   __AUTH_CONST.__const: 0x9420
-  __AUTH_CONST.__cfstring: 0xbac0
+  __AUTH_CONST.__cfstring: 0xba80
   __AUTH_CONST.__objc_const: 0x1550
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1e40
+  __AUTH_CONST.__auth_got: 0x1e38
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x174
   __DATA.__data: 0x17c40
   __DATA.__common: 0xa80
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x380
-  __DATA_DIRTY.__bss: 0x1a8
+  __DATA_DIRTY.__bss: 0x1c0
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1706
-  Symbols:   3588
-  CStrings:  5203
+  Functions: 1715
+  Symbols:   3606
+  CStrings:  5207
 
Symbols:
+ GCC_except_table101
+ GCC_except_table1014
+ GCC_except_table105
+ GCC_except_table107
+ GCC_except_table110
+ GCC_except_table1127
+ GCC_except_table113
+ GCC_except_table1146
+ GCC_except_table115
+ GCC_except_table119
+ GCC_except_table1197
+ GCC_except_table1201
+ GCC_except_table124
+ GCC_except_table1254
+ GCC_except_table1262
+ GCC_except_table1264
+ GCC_except_table127
+ GCC_except_table128
+ GCC_except_table1308
+ GCC_except_table132
+ GCC_except_table1371
+ GCC_except_table148
+ GCC_except_table151
+ GCC_except_table152
+ GCC_except_table156
+ GCC_except_table159
+ GCC_except_table166
+ GCC_except_table167
+ GCC_except_table183
+ GCC_except_table194
+ GCC_except_table218
+ GCC_except_table225
+ GCC_except_table231
+ GCC_except_table419
+ GCC_except_table482
+ GCC_except_table532
+ GCC_except_table592
+ GCC_except_table596
+ GCC_except_table603
+ GCC_except_table611
+ GCC_except_table748
+ GCC_except_table85
+ GCC_except_table89
+ _APSIsHomeAccessory
+ __ShouldUseHardwareVolume
+ ___getMRNowPlayingInfoMediaTypeAudioSymbolLoc_block_invoke
+ ___getMRNowPlayingInfoMediaTypeVideoSymbolLoc_block_invoke
+ ___getkMRMediaRemoteNowPlayingInfoStrictMediaTypeSymbolLoc_block_invoke
+ ___getkMRMediaRemoteNowPlayingInfoTypeAudioSymbolLoc_block_invoke
+ ___getkMRMediaRemoteNowPlayingInfoTypeVideoSymbolLoc_block_invoke
+ _getMRNowPlayingInfoMediaTypeAudioSymbolLoc.ptr
+ _getMRNowPlayingInfoMediaTypeVideo
+ _getMRNowPlayingInfoMediaTypeVideoSymbolLoc.ptr
+ _getkMRMediaRemoteNowPlayingInfoMediaType
+ _getkMRMediaRemoteNowPlayingInfoStrictMediaType
+ _getkMRMediaRemoteNowPlayingInfoStrictMediaTypeSymbolLoc.ptr
+ _getkMRMediaRemoteNowPlayingInfoTypeAudioSymbolLoc.ptr
+ _getkMRMediaRemoteNowPlayingInfoTypeVideo
+ _getkMRMediaRemoteNowPlayingInfoTypeVideoSymbolLoc.ptr
- GCC_except_table1005
- GCC_except_table104
- GCC_except_table106
- GCC_except_table109
- GCC_except_table1118
- GCC_except_table112
- GCC_except_table1137
- GCC_except_table114
- GCC_except_table117
- GCC_except_table1188
- GCC_except_table1192
- GCC_except_table123
- GCC_except_table1245
- GCC_except_table1253
- GCC_except_table1255
- GCC_except_table1299
- GCC_except_table134
- GCC_except_table1362
- GCC_except_table139
- GCC_except_table142
- GCC_except_table150
- GCC_except_table157
- GCC_except_table158
- GCC_except_table174
- GCC_except_table185
- GCC_except_table207
- GCC_except_table209
- GCC_except_table222
- GCC_except_table411
- GCC_except_table474
- GCC_except_table523
- GCC_except_table583
- GCC_except_table587
- GCC_except_table594
- GCC_except_table602
- GCC_except_table739
- GCC_except_table88
- GCC_except_table99
- _AirPlayManagedDefaultsLogging_HandleReceiverManagedDefaultsLoggingChanged
- _CFPreferencesAppSynchronize
- _LogControlCF
CStrings:
+ "-[AirPlayReceiverMediaRemoteHelper setMRNowPlayingInfo:withMergePolicy:]"
+ "1005.13.1.1"
+ "MRNowPlayingInfoMediaTypeAudio"
+ "MRNowPlayingInfoMediaTypeVideo"
+ "[%{ptr}] Overriding media type from video to audio.\n"
+ "kMRMediaRemoteNowPlayingInfoStrictMediaType"
+ "kMRMediaRemoteNowPlayingInfoTypeAudio"
+ "kMRMediaRemoteNowPlayingInfoTypeVideo"
- "1005.12.1"
- "AirPlayServerLoggingLevel"
- "AirPlayServerLoggingOutput"
- "MediaControlSenderLogControlCF"
```
