## CardioHealth

> `/System/Library/PrivateFrameworks/CardioHealth.framework/CardioHealth`

```diff

-3075.0.8.0.0
-  __TEXT.__text: 0xd560
-  __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__const: 0x530
-  __TEXT.__gcc_except_tab: 0x4c0
-  __TEXT.__cstring: 0x20f
-  __TEXT.__oslogstring: 0x2539
-  __TEXT.__unwind_info: 0x270
-  __TEXT.__objc_methname: 0x66
-  __TEXT.__objc_stubs: 0xa0
-  __DATA_CONST.__got: 0x50
+3164.0.0.0.0
+  __TEXT.__text: 0xe4fc
+  __TEXT.__const: 0x550
+  __TEXT.__gcc_except_tab: 0x3b4
+  __TEXT.__cstring: 0x18f6
+  __TEXT.__oslogstring: 0x2558
+  __TEXT.__unwind_info: 0x2a0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__objc_selrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x100
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x130
   __AUTH_CONST.__cfstring: 0x40
+  __AUTH_CONST.__weak_auth_got: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __DATA_DIRTY.__data: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 15895043-E14F-33A4-B952-E1660D8D5E54
-  Functions: 91
-  Symbols:   88
-  CStrings:  103
+  UUID: 2503EEDF-489F-323E-A101-A8605CB43049
+  Functions: 102
+  Symbols:   87
+  CStrings:  111
 
Symbols:
+ __ZN12CardioHealth21isExtendedWorkoutModeENS_13CHWorkoutModeE
+ __ZNSt3__132__internal_log_hardening_failureEPKc
- __os_signpost_emit_with_name_impl
- _abort_report_np
- _os_signpost_enabled
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1156: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:413: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:418: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:441: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:1577: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:2199: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "VO2Max,AdaptiveOutdoorPedestrianModel,Invalid clustering results: clusterIdx=%{public}u maxNumClusters=%{public}u inputIdx=%{public}u inputsSize=%{public}zu"
+ "VO2Max,deriveStageBasedClusters,Negative stage value %{public}d at input index %{public}zu"
+ "prior,%f,hrMin,%f,hrMax,%f,metsResponseRate,%f,metsRecoveryRate,%{public}f,clusteringMode,%{public}d,numPairs,%{public}d"
- "%s:%d: assertion failure in %s"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocation/Framework/CardioHealth/Models/CHVO2MaxAdaptiveOutdoorPedestrianModel.mm"
- "VO2Max,AdaptiveOutdoorPedestrianModel,Invalid clustering results."
- "assert"
- "clusterIdx < maxNumClusters || inputIdx < inputsToCluster.size()"
- "code"
- "dictionaryWithObjects:forKeys:count:"
- "errorWithDomain:code:userInfo:"
- "localTimeZone"
- "populateClusters"
- "prior,%f,hrMin,%f,hrMax,%f,metsResponseRate,%f,metsRecoveryRate,%{public}f,numPairs,%{public}d"
- "secondsFromGMT"
- "{\"msg%{public}.0s\":\"VO2Max,AdaptiveOutdoorPedestrianModel,Invalid clustering results.\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"

```
