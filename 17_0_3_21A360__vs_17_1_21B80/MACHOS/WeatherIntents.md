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
