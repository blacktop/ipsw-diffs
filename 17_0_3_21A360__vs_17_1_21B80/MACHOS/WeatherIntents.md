## WeatherIntents

> `/private/var/staged_system_apps/Weather.app/PlugIns/WeatherIntents.appex/WeatherIntents`

```diff

-469.4.0.0.0
-  __TEXT.__text: 0xc24c
+484.0.0.0.0
+  __TEXT.__text: 0xc2b0
   __TEXT.__auth_stubs: 0xda0
   __TEXT.__objc_stubs: 0x140
   __TEXT.__objc_methlist: 0x210

   __TEXT.__objc_methname: 0x72b
   __TEXT.__objc_methtype: 0x146
   __TEXT.__const: 0x3a2
-  __TEXT.__cstring: 0xd76
+  __TEXT.__cstring: 0xdc6
   __TEXT.__swift5_typeref: 0x3f2
   __TEXT.__constg_swiftt: 0x2b4
   __TEXT.__swift5_reflstr: 0x28f

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DA5418A1-EDB6-3B1F-A767-9E9A01626360
+  UUID: 2D65B4D1-8AFC-3E07-A373-4496D77B5AE5
   Functions: 332
   Symbols:   141
   CStrings:  195
CStrings:
+ "Failed to geocode. searchString=%{sensitive,mask.hash}s, error=%{public}s"
+ "Received an error while requesting a local search completion. searchQuery=%{sensitive,mask.hash}s, error=%{public}s"
+ "Successfully geocoded location. searchString=%{sensitive,mask.hash}s, location=%{private,mask.hash}s, unsanitizedSecondaryName=%{private,mask.hash}s"
+ "Time zone missing while geocoding, searchString=%{sensitive,mask.hash}s."
+ "`MKMapItem` missing while geocoding. searchString=%{sensitive,mask.hash}s."
- "Failed to geocode. searchString=%{public}s, error=%{public}s"
- "Received an error while requesting a local search completion. searchQuery=%{public}s, error=%{public}s"
- "Successfully geocoded location. searchString=%{public}s, location=%{private,mask.hash}s, unsanitizedSecondaryName=%{private,mask.hash}s"
- "Time zone missing while geocoding, searchString=%{public}s."
- "`MKMapItem` missing while geocoding. searchString=%{public}s."

```
