## NetworkStatistics

> `/System/Library/PrivateFrameworks/NetworkStatistics.framework/NetworkStatistics`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-279.60.2.0.0
-  __TEXT.__text: 0x2f02c
-  __TEXT.__objc_methlist: 0x4a60
+279.60.3.0.0
+  __TEXT.__text: 0x2f96c
+  __TEXT.__objc_methlist: 0x4a90
   __TEXT.__cstring: 0x7466
-  __TEXT.__oslogstring: 0x26c8
-  __TEXT.__const: 0x210
+  __TEXT.__oslogstring: 0x2aa2
+  __TEXT.__const: 0x220
   __TEXT.__gcc_except_tab: 0x37c
-  __TEXT.__unwind_info: 0xf18
+  __TEXT.__unwind_info: 0xf30
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1df8
+  __DATA_CONST.__objc_selrefs: 0x1e18
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0x8b8
   __DATA_CONST.__got: 0x1c0
-  __AUTH_CONST.__const: 0x120
+  __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__cfstring: 0x6820
-  __AUTH_CONST.__objc_const: 0x8b30
+  __AUTH_CONST.__objc_const: 0x8bf0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x810
+  __DATA.__objc_ivar: 0x824
   __DATA.__data: 0x508
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xfa0

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1708
-  Symbols:   3036
-  CStrings:  1303
+  Functions: 1716
+  Symbols:   3051
+  CStrings:  1317
 
Symbols:
+ -[NWStatsManager _handleCompletion:failed:]
+ -[NWStatsManager nextPollReference]
+ -[NWStatsManager setNextPollReference:]
+ -[NWStatsPollHandler completionFailed]
+ -[NWStatsPollHandler setCompletionFailed:]
+ _NWStatsMachTicksFromSeconds
+ _NWStatsTimebaseInfo.onceToken
+ _NWStatsTimebaseInfo.timebaseInfo
+ _OBJC_IVAR_$_NWStatsManager._pollProgressGeneration
+ _OBJC_IVAR_$_NWStatsManager._syncWaitKqueueArmed
+ _OBJC_IVAR_$_NWStatsManager._syncWaitKqueueFd
+ _OBJC_IVAR_$_NWStatsManager._syncWaitReadFilterRegistered
+ _OBJC_IVAR_$_NWStatsPollHandler._completionFailed
+ ___NWStatsTimebaseInfo_block_invoke
+ _kevent
+ _kqueue
- -[NWStatsManager _handleCompletion:]
CStrings:
+ "Poll request failed with kernel error %d, unsticking poll, context %lld"
+ "_refreshSyncUsingBlock kevent() failed, errno %d"
+ "_refreshSyncUsingBlock kevent() failure while waiting for a reply, context %llu"
+ "_refreshSyncUsingBlock kevent() failure while waiting for an earlier poll to finish"
+ "_refreshSyncUsingBlock kevent() registration failed, errno %d"
+ "_refreshSyncUsingBlock kevent() reported an error, errno %ld"
+ "_refreshSyncUsingBlock kevent() reported data %u times with nothing read - treating as a dead socket"
+ "_refreshSyncUsingBlock kqueue() failed, errno %d"
+ "_refreshSyncUsingBlock poll completed via a failure path, context %llu"
+ "_refreshSyncUsingBlock skipped as current outstanding is %d"
+ "_refreshSyncUsingBlock timed out after %.1fs of inactivity waiting for a reply, context %llu"
+ "_refreshSyncUsingBlock timed out after %.1fs of inactivity waiting for an earlier poll to finish"
+ "_sendMessage attempted with no readSource, context %lld"
+ "_sendMessage send() failed, errno %d, context %lld"
+ "\xf0\xf0\xf0\xf0\xd1"
+ "\xf0\xf0\xf0\xf0\xe5E"
- "\xf0\xf0\xf0\xf0\xb1"
- "\xf0\xf0\xf0\xf0\xc5E"
```
