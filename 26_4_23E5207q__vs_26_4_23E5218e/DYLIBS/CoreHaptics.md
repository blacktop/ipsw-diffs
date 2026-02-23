## CoreHaptics

> `/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`

```diff

-272.501.0.0.0
-  __TEXT.__text: 0x5717c
+272.502.0.0.0
+  __TEXT.__text: 0x572e8
   __TEXT.__auth_stubs: 0xcd0
   __TEXT.__objc_methlist: 0x245c
   __TEXT.__const: 0x528
-  __TEXT.__gcc_except_tab: 0x9b54
-  __TEXT.__cstring: 0x71b3
+  __TEXT.__gcc_except_tab: 0x9b8c
+  __TEXT.__cstring: 0x71de
   __TEXT.__oslogstring: 0x8af2
   __TEXT.__unwind_info: 0x1d98
   __TEXT.__objc_classname: 0x3b8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CC68C12C-D586-35FC-B7E6-09EFAA144D29
-  Functions: 1067
-  Symbols:   4257
-  CStrings:  2930
+  UUID: 78006FA3-AC8B-3063-80A0-CCD3915E06FB
+  Functions: 1068
+  Symbols:   4259
+  CStrings:  2931
 
Symbols:
+ GCC_except_table129
+ GCC_except_table132
+ GCC_except_table148
+ GCC_except_table154
+ GCC_except_table185
+ GCC_except_table187
+ GCC_except_table198
+ GCC_except_table200
+ GCC_except_table203
+ GCC_except_table210
+ GCC_except_table221
+ ___29-[CHHapticEngine finishInit:]_block_invoke.188
+ ___31-[CHHapticEngine handleFinish:]_block_invoke.195
+ ___32-[CHHapticEngine beginIdleTimer]_block_invoke.191
+ ___38-[CHHapticEngine doPlayPattern:error:]_block_invoke.247
+ ___39-[CHHapticEngine doStartEngineAndWait:]_block_invoke.227
+ ___41-[CHHapticEngine handleMediaServerDeath:]_block_invoke
+ ___44-[CHHapticEngine handleMediaServerRecovery:]_block_invoke.178
+ ___45-[CHHapticEngine startWithCompletionHandler:]_block_invoke.226
+ ___46-[CHHapticEngine doStopWithCompletionHandler:]_block_invoke.231
+ ___47-[CHHapticEngine doStartWithCompletionHandler:]_block_invoke.223
+ ___92-[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:error:]_block_invoke.488
+ ___92-[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:error:]_block_invoke.493
+ ___block_literal_global.217
+ ___block_literal_global.229
- GCC_except_table149
- GCC_except_table175
- GCC_except_table184
- GCC_except_table186
- GCC_except_table190
- GCC_except_table199
- GCC_except_table201
- GCC_except_table206
- GCC_except_table219
- ___29-[CHHapticEngine finishInit:]_block_invoke.185
- ___31-[CHHapticEngine handleFinish:]_block_invoke.191
- ___32-[CHHapticEngine beginIdleTimer]_block_invoke.189
- ___38-[CHHapticEngine doPlayPattern:error:]_block_invoke.246
- ___39-[CHHapticEngine doStartEngineAndWait:]_block_invoke.226
- ___44-[CHHapticEngine stopWithCompletionHandler:]_block_invoke.231
- ___45-[CHHapticEngine startWithCompletionHandler:]_block_invoke.225
- ___46-[CHHapticEngine doStopWithCompletionHandler:]_block_invoke.229
- ___47-[CHHapticEngine doStartWithCompletionHandler:]_block_invoke.221
- ___92-[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:error:]_block_invoke.487
- ___92-[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:error:]_block_invoke.492
- ___block_literal_global.216
- ___block_literal_global.228
Functions:
- ___29-[CHHapticEngine finishInit:]_block_invoke.185
- ___92-[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:error:]_block_invoke.487
~ -[CHHapticEngine stopWithCompletionHandler:] : 912 -> 696
- ___47-[CHHapticEngine doStartWithCompletionHandler:]_block_invoke.221
~ -[CHHapticEngine handleMediaServerDeath:] : 516 -> 656
+ ___41-[CHHapticEngine handleMediaServerDeath:]_block_invoke
~ ___44-[CHHapticEngine handleMediaServerRecovery:]_block_invoke : 2120 -> 2276
+ ___44-[CHHapticEngine handleMediaServerRecovery:]_block_invoke.178
~ ___29-[CHHapticEngine finishInit:]_block_invoke.186 : 412 -> 532
~ ___29-[CHHapticEngine finishInit:]_block_invoke.187 : 496 -> 412
+ ___29-[CHHapticEngine finishInit:]_block_invoke.188
~ ___47-[CHHapticEngine doStartWithCompletionHandler:]_block_invoke.222 : 308 -> 616
+ ___47-[CHHapticEngine doStartWithCompletionHandler:]_block_invoke.223
~ ___44-[CHHapticEngine stopWithCompletionHandler:]_block_invoke : 32 -> 608
- ___44-[CHHapticEngine stopWithCompletionHandler:]_block_invoke.231
~ -[CHHapticEngine doUnregisterAllPublicAudioResources] : 432 -> 468
~ ___69-[CHHapticEngine(CHHapticEngineInternal) notifyPlayerStarted:atTime:]_block_invoke_2 : 640 -> 636
+ ___92-[CHHapticEngine(CHHapticEngineInternal) doRegisterAudioResource:options:fromPattern:error:]_block_invoke.493
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CI69ugBvLbUNv0ENMAj9LMz_O70n39MQplP1_uI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CI69ugBvLbUNv0ENMAj9LMz_O70n39MQplP1_uI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CI69ugBvLbUNv0ENMAj9LMz_O70n39MQplP1_uI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CI69ugBvLbUNv0ENMAj9LMz_O70n39MQplP1_uI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "/Library/Caches/com.apple.xbs/91B0A05A-14C0-49E8-8F2F-F2632CB31547/TemporaryDirectory.Pzdk74/Sources/CoreHaptics/Source/AVHapticPlayer.mm"
+ "/Library/Caches/com.apple.xbs/91B0A05A-14C0-49E8-8F2F-F2632CB31547/TemporaryDirectory.Pzdk74/Sources/CoreHaptics/Source/CHHapticAdvancedPatternPlayer.mm"
+ "/Library/Caches/com.apple.xbs/91B0A05A-14C0-49E8-8F2F-F2632CB31547/TemporaryDirectory.Pzdk74/Sources/CoreHaptics/Source/CHHapticEngine.mm"
+ "/Library/Caches/com.apple.xbs/91B0A05A-14C0-49E8-8F2F-F2632CB31547/TemporaryDirectory.Pzdk74/Sources/CoreHaptics/Source/CHHapticPatternPlayer.mm"
+ "strongSelf && (strongSelf->_player != nil)"
- "/AppleInternal/Library/BuildRoots/4~CHoNugDNGwWYoQRXdpJMUWfBa9ggcNfXuMvWTgo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CHoNugDNGwWYoQRXdpJMUWfBa9ggcNfXuMvWTgo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CHoNugDNGwWYoQRXdpJMUWfBa9ggcNfXuMvWTgo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CHoNugDNGwWYoQRXdpJMUWfBa9ggcNfXuMvWTgo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
- "/Library/Caches/com.apple.xbs/E4F32DE6-8981-4754-BE80-B3A83306BBA6/TemporaryDirectory.qS2b51/Sources/CoreHaptics/Source/AVHapticPlayer.mm"
- "/Library/Caches/com.apple.xbs/E4F32DE6-8981-4754-BE80-B3A83306BBA6/TemporaryDirectory.qS2b51/Sources/CoreHaptics/Source/CHHapticAdvancedPatternPlayer.mm"
- "/Library/Caches/com.apple.xbs/E4F32DE6-8981-4754-BE80-B3A83306BBA6/TemporaryDirectory.qS2b51/Sources/CoreHaptics/Source/CHHapticEngine.mm"
- "/Library/Caches/com.apple.xbs/E4F32DE6-8981-4754-BE80-B3A83306BBA6/TemporaryDirectory.qS2b51/Sources/CoreHaptics/Source/CHHapticPatternPlayer.mm"

```
