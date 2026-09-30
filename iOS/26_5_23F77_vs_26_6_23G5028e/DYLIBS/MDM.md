## MDM

> `/System/Library/PrivateFrameworks/MDM.framework/MDM`

```diff

-59.120.4.0.0
-  __TEXT.__text: 0x594f8
+59.160.4.0.0
+  __TEXT.__text: 0x59a30
   __TEXT.__auth_stubs: 0xf10
-  __TEXT.__objc_methlist: 0x41cc
-  __TEXT.__const: 0x1aa
-  __TEXT.__gcc_except_tab: 0x10b4
-  __TEXT.__cstring: 0x56d9
-  __TEXT.__oslogstring: 0x6e47
+  __TEXT.__objc_methlist: 0x41e4
+  __TEXT.__const: 0x1ba
+  __TEXT.__gcc_except_tab: 0x10e4
+  __TEXT.__cstring: 0x5707
+  __TEXT.__oslogstring: 0x71ad
   __TEXT.__dlopen_cstrs: 0x55
   __TEXT.__swift5_typeref: 0x3c
   __TEXT.__swift5_capture: 0x68
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0x1450
+  __TEXT.__unwind_info: 0x1458
   __TEXT.__eh_frame: 0x178
   __TEXT.__objc_classname: 0x6e3
-  __TEXT.__objc_methname: 0xedc4
+  __TEXT.__objc_methname: 0xee17
   __TEXT.__objc_methtype: 0x1b8a
-  __TEXT.__objc_stubs: 0xbb20
+  __TEXT.__objc_stubs: 0xbb60
   __DATA_CONST.__got: 0x11d0
   __DATA_CONST.__const: 0x1f10
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x34d8
+  __DATA_CONST.__objc_selrefs: 0x34e8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x68
   __AUTH_CONST.__auth_got: 0x798
   __AUTH_CONST.__const: 0x610
-  __AUTH_CONST.__cfstring: 0x5140
+  __AUTH_CONST.__cfstring: 0x5160
   __AUTH_CONST.__objc_const: 0x6a90
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x138

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: AFCC7F2B-FE98-3086-BF52-CB26876BEA75
-  Functions: 1660
-  Symbols:   6701
-  CStrings:  4293
+  UUID: 0CA9369B-7304-3737-9C8A-6DF595A87E79
+  Functions: 1664
+  Symbols:   6711
+  CStrings:  4308
 
Symbols:
+ -[MDMServerCore _memberQueuePollForHRNFromBackgroundTask:]
+ -[MDMServerCore _memberQueuePollOrScheduleNextPollForHRN]
+ GCC_except_table283
+ GCC_except_table290
+ GCC_except_table301
+ GCC_except_table312
+ GCC_except_table327
+ GCC_except_table342
+ GCC_except_table358
+ ___57-[MDMServerCore _memberQueuePollOrScheduleNextPollForHRN]_block_invoke
+ ___57-[MDMServerCore _memberQueuePollOrScheduleNextPollForHRN]_block_invoke_2
+ ___58-[MDMServerCore _memberQueuePollForHRNFromBackgroundTask:]_block_invoke
+ ___58-[MDMServerCore _memberQueuePollForHRNFromBackgroundTask:]_block_invoke_2
+ ___block_literal_global.388
+ _objc_msgSend$_memberQueuePollForHRNFromBackgroundTask:
+ _objc_msgSend$_memberQueuePollOrScheduleNextPollForHRN
- GCC_except_table279
- GCC_except_table286
- GCC_except_table297
- GCC_except_table308
- GCC_except_table319
- GCC_except_table334
- GCC_except_table354
- ___76-[MDMServerCore _memberQueuePollOrScheduleNextPollForHRNFromBackgroundTask:]_block_invoke
- ___76-[MDMServerCore _memberQueuePollOrScheduleNextPollForHRNFromBackgroundTask:]_block_invoke_2
- ___block_literal_global.385
CStrings:
+ "(nil)"
+ "-[MDMServerCore _memberQueuePollForHRNFromBackgroundTask:]"
+ "-[MDMServerCore _memberQueuePollOrScheduleNextPollForHRN]"
+ "Device is on seed build. Skip the random delay"
+ "MDMServerCore HRN polling now (first poll)..."
+ "MDMServerCore HRN polling now (from background task)..."
+ "MDMServerCore HRN scheduling next poll in %{public}f seconds..."
+ "MDMServerCore _memberQueueParseMDMConfigurationDict: after hrnMode switch, pollingInterval=%@"
+ "MDMServerCore _memberQueueParseMDMConfigurationDict: hrnMode=%d (0=Unknown, 1=No, 2=Yes)"
+ "MDMServerCore _memberQueuePollOrScheduleNextPollForHRN: pollingIntervalMinutes=%lu, pollingInterval=%@, fromBackgroundTask=%d"
+ "MDMServerCore _pollOrScheduleNextPollForHRN: entering (isSharediPad=NO)"
+ "MDMServerCore _pollOrScheduleNextPollForHRN: skipping because isSharediPad=YES"
+ "MDMServerCore _readConfigurationOutError: calling _pollOrScheduleNextPollForHRN (valid=%d)"
+ "MDMServerCore _readConfigurationOutError: skipping HRN poll (channelType=%d, not device)"
+ "MDMServerCore _scheduleNextPollWithInterval: interval=%{public}f, targetPollDate=%{public}@"
+ "_memberQueuePollForHRNFromBackgroundTask:"
+ "_memberQueuePollOrScheduleNextPollForHRN"
- "-[MDMServerCore _memberQueuePollOrScheduleNextPollForHRNFromBackgroundTask:]"
- "MDMServerCore HRN polling now..."
- "MDMServerCore HRN scheduling next poll..."

```
