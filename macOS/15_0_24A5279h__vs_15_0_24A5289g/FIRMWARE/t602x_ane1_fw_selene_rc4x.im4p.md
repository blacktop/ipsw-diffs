## t602x_ane1_fw_selene_rc4x.im4p

> `t602x_ane1_fw_selene_rc4x.im4p`

```diff

 
-  __TEXT.__text: 0xa6588
+  __TEXT.__text: 0xa6d98
   __TEXT.__data_copy: 0x8000
   __TEXT.__const: 0x38388
-  __TEXT.__cstring: 0x1ad4c
+  __TEXT.__cstring: 0x1ad58
   __TEXT._rtk_mtab: 0x2a0
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT.text_env: 0x28
-  __DATA.__const: 0x5200
+  __DATA.__const: 0x5210
   __DATA._rtk_heap: 0x1000
   __DATA.__data: 0xfc8
   __DATA._rtk_patchbay: 0x1e8

   __DATA.__zerofill: 0x53eb0
   Functions: 0
   Symbols:   0
-  CStrings:  3283
+  CStrings:  3286
 
CStrings:
+ "\x1b[31m\"[ABORT] Suspend other TQs for TQ[%!d(MISSING)]S[%!d(MISSING)] at %!l(MISSING)ld\"\x1b[39m"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/common/CEispInterruptBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/common/msgQ.c"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/rtxc/CWorkTask.cpp"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/rtxc/memObj.cpp"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/rtxc/mutex.cpp"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/rtxc/sema.cpp"
+ "20:45:27"
+ "Dummy network NID %!d(MISSING) TD Complete event %!l(MISSING)ld"
+ "Enable TQs after Dummy network finish in TQ[%!d(MISSING)]"
+ "Enable TQs after letting TQ[%!d(MISSING)] finish"
+ "Function should be overridden and not supported"
+ "Jun 27 2024"
+ "SetTQState"
+ "Setting TQ[%!d(MISSING)] to invalid TQ state %!d(MISSING)"
+ "Suspend TQs for Dummy Network"
+ "state < MAX_NUM_ANE_TQ_STATE"
- "\x1b[31m\"    Restore Matched Priority Q[%!d(MISSING)]S[%!d(MISSING)] is done. Dummy %!d(MISSING)\"\x1b[39m"
- "\x1b[31m\"[ABORT] raise priority Q[%!d(MISSING)]S[%!d(MISSING)] at %!l(MISSING)ld\"\x1b[39m"
- "!reqRunning[foundIndex][slot].isAborting"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/common/CEispInterruptBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/common/msgQ.c"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/rtxc/CWorkTask.cpp"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/rtxc/memObj.cpp"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/rtxc/mutex.cpp"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleAneFW/sne/ssi/src/rtxc/sema.cpp"
- "13:27:36"
- "Dummy network NID %!d(MISSING) Finish event %!l(MISSING)ld"
- "Jun 15 2024"
- "reqRunning[foundIndex][slot].isAborting || reqRunning[foundIndex][slot].isDummyNetwork"
- "tqPrty.f.TQPriority == queuePriority[queueId]"

```
