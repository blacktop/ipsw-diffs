## coreaudiod

> `/usr/sbin/coreaudiod`

```diff

-  __TEXT.__text: 0x1a3fc
+  __TEXT.__text: 0x1a314
   __TEXT.__auth_stubs: 0xb20
   __TEXT.__const: 0xbf0
   __TEXT.__gcc_except_tab: 0x1cbc
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__bss : content changed
Functions:
~ __ZN25AHS_DeviceSettingsManagerD1Ev : 1696 -> 1624
~ __ZN25AHS_DeviceSettingsManager12SaveSettingsEv : 4728 -> 4680
~ __ZNSt3__111basic_regexIcNS_12regex_traitsIcEEE26__parse_bracket_expressionIPKcEET_S7_S7_ : 3324 -> 3308
~ __ZNSt3__111basic_regexIcNS_12regex_traitsIcEEE24__parse_collating_symbolIPKcEET_S7_S7_RNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE : 224 -> 212
~ __ZN4AMCP7Utility22With_Realtime_DisabledC2Ev : 2180 -> 2152
~ __ZN4AMCP7Utility22With_Realtime_DisabledD2Ev : 888 -> 876
~ _main : 6288 -> 6284
~ __ZN4AMCP7Utility9Mach_Port11create_portEj : 1248 -> 1228
~ __ZN4AMCP7Utility9Mach_Port19set_receive_handlerERKN10applesauce8dispatch2v15queueENSt3__18functionIFvvEEE : 1148 -> 1128
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UUmNaE/Sources/AudioHAL/MCP/AMCP/Utility/Mach_Port.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UUmNaE/Sources/AudioHAL/MCP/AMCP/Utility/Thread_Utilities.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UUmNaE/Sources/AudioHAL/Source/coreaudiod/AHS_DeviceSettings.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwLYKQ/Sources/AudioHAL/MCP/AMCP/Utility/Mach_Port.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwLYKQ/Sources/AudioHAL/MCP/AMCP/Utility/Thread_Utilities.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwLYKQ/Sources/AudioHAL/Source/coreaudiod/AHS_DeviceSettings.cpp"

```
