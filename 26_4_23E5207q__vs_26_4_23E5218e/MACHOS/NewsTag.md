## NewsTag

> `/private/var/staged_system_apps/News.app/PlugIns/NewsTag.appex/NewsTag`

```diff

-5861.1.0.0.0
-  __TEXT.__text: 0xa0c24
+5864.0.0.0.0
+  __TEXT.__text: 0xa0f2c
   __TEXT.__auth_stubs: 0x3090
   __TEXT.__objc_stubs: 0x4e20
   __TEXT.__objc_methlist: 0x2318

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F6E0B87D-CAAB-3DD2-B860-5544B5EE4888
+  UUID: 23916CDD-3507-3A8B-940E-B3ACEC727870
   Functions: 2879
   Symbols:   593
   CStrings:  2038
Functions:
~ sub_100029364 : 1584 -> 1556
~ sub_100029b14 -> sub_100029af8 : 1648 -> 1632
~ sub_10002cf54 -> sub_10002cf28 : 4620 -> 4608
~ sub_100032480 -> sub_100032448 : 640 -> 704
~ sub_100032700 -> sub_100032708 : 4832 -> 5020
~ sub_10003e578 -> sub_10003e63c : 440 -> 432
~ sub_1000578dc -> sub_100057998 : 4456 -> 4728
~ sub_10005af60 -> sub_10005b12c : 5876 -> 6096
~ sub_1000645e4 -> sub_10006488c : 780 -> 924
~ sub_1000670f4 -> sub_10006742c : 88 -> 96
~ sub_10006714c -> sub_10006748c : 96 -> 88
~ sub_1000768e0 -> sub_100076c18 : 744 -> 732
~ sub_100076d88 -> sub_1000770b4 : 456 -> 444
~ sub_10007bac0 -> sub_10007bde0 : 2120 -> 2088
~ sub_10008e158 -> sub_10008e458 : 1152 -> 1160
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJJsugDH50afcjaOL7as7H89UXgykpKOvMJQCIs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJJsugDH50afcjaOL7as7H89UXgykpKOvMJQCIs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJJsugDH50afcjaOL7as7H89UXgykpKOvMJQCIs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJJsugDH50afcjaOL7as7H89UXgykpKOvMJQCIs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJJsugDH50afcjaOL7as7H89UXgykpKOvMJQCIs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJJsugDH50afcjaOL7as7H89UXgykpKOvMJQCIs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJJsugDH50afcjaOL7as7H89UXgykpKOvMJQCIs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJJsugDH50afcjaOL7as7H89UXgykpKOvMJQCIs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJJsugDH50afcjaOL7as7H89UXgykpKOvMJQCIs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJJsugDH50afcjaOL7as7H89UXgykpKOvMJQCIs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Classes/FRNewsReferralItemEncoding.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Classes/FRNewsReferralItemWidgetArticleList.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Classes/FRReferredArticle.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FRNewsReferralItemWidgetArticleList+FTAdditions.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTAggregateWidgetEventTracker.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTBackgroundEngagementDescriptor.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTBannerEngagementDescriptor.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTConditionalWidgetEventTracker.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTConstants.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTEngagementURLProvider.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTEventTrackingConstants.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTHeaderEngagementDescriptor.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTHeadlineEngagementEventTracker.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTHeadlineRowOpenURLEngagementDescriptor.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTNewsAnalyticsNonVideoContentTypeWidgetEventTracker.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTNewsAnalyticsWidgetEventTracker.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTNewsModeProactiveWidgetEventTracker.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTNonNewsModeProactiveWidgetEventTracker.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTOpenArbitraryURLEngagementDescriptor.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTPlaceholderEngagementDescriptor.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTProactiveWidgetEventTracker.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTSeenHeadlineWidgetEventTracker.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTWidgetAppearanceEventTracker.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTWidgetLingerEventTracker.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTWidgetUpdateEventTracker.m"
+ "/Library/Caches/com.apple.xbs/5B972533-7BF1-4F41-98F1-72E3E14F314F/TemporaryDirectory.GO6mlX/Sources/Feldspar/feldspar/Extensions/FeldsparToday/NSURL+FTReferralAdditions.m"
- "/AppleInternal/Library/BuildRoots/4~CIZpugBCaAK-j0e-OhnoizyTvGD6c1SzgiznzZU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIZpugBCaAK-j0e-OhnoizyTvGD6c1SzgiznzZU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIZpugBCaAK-j0e-OhnoizyTvGD6c1SzgiznzZU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIZpugBCaAK-j0e-OhnoizyTvGD6c1SzgiznzZU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIZpugBCaAK-j0e-OhnoizyTvGD6c1SzgiznzZU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIZpugBCaAK-j0e-OhnoizyTvGD6c1SzgiznzZU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIZpugBCaAK-j0e-OhnoizyTvGD6c1SzgiznzZU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIZpugBCaAK-j0e-OhnoizyTvGD6c1SzgiznzZU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIZpugBCaAK-j0e-OhnoizyTvGD6c1SzgiznzZU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIZpugBCaAK-j0e-OhnoizyTvGD6c1SzgiznzZU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Classes/FRNewsReferralItemEncoding.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Classes/FRNewsReferralItemWidgetArticleList.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Classes/FRReferredArticle.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FRNewsReferralItemWidgetArticleList+FTAdditions.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTAggregateWidgetEventTracker.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTBackgroundEngagementDescriptor.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTBannerEngagementDescriptor.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTConditionalWidgetEventTracker.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTConstants.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTEngagementURLProvider.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTEventTrackingConstants.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTHeaderEngagementDescriptor.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTHeadlineEngagementEventTracker.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTHeadlineRowOpenURLEngagementDescriptor.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTNewsAnalyticsNonVideoContentTypeWidgetEventTracker.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTNewsAnalyticsWidgetEventTracker.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTNewsModeProactiveWidgetEventTracker.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTNonNewsModeProactiveWidgetEventTracker.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTOpenArbitraryURLEngagementDescriptor.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTPlaceholderEngagementDescriptor.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTProactiveWidgetEventTracker.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTSeenHeadlineWidgetEventTracker.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTWidgetAppearanceEventTracker.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTWidgetLingerEventTracker.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Extensions/FeldsparToday/FTWidgetUpdateEventTracker.m"
- "/Library/Caches/com.apple.xbs/CC554B5B-4750-4C7F-9996-7B40743F4FA9/TemporaryDirectory.6SYy3T/Sources/Feldspar/feldspar/Extensions/FeldsparToday/NSURL+FTReferralAdditions.m"

```
