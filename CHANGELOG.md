# Changelog

## [0.14.2](https://github.com/googleapis/python-analytics-data/compare/v0.14.1...v0.14.2) (2022-10-10)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#303](https://github.com/googleapis/python-analytics-data/issues/303)) ([6eadb8c](https://github.com/googleapis/python-analytics-data/commit/6eadb8c08ebd49f466bad1fddfcf2165a1be719d))
* **deps:** require google-api-core&gt;=1.33.2 ([6eadb8c](https://github.com/googleapis/python-analytics-data/commit/6eadb8c08ebd49f466bad1fddfcf2165a1be719d))

## [0.14.1](https://github.com/googleapis/python-analytics-data/compare/v0.14.0...v0.14.1) (2022-09-30)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#297](https://github.com/googleapis/python-analytics-data/issues/297)) ([d0d59ea](https://github.com/googleapis/python-analytics-data/commit/d0d59eae7d0a9cdb29c7668ddec54ca077939bfd))

## [0.14.0](https://github.com/googleapis/python-analytics-data/compare/v0.13.2...v0.14.0) (2022-09-19)


### Features

* Add support for REST transport ([#290](https://github.com/googleapis/python-analytics-data/issues/290)) ([1e4f58e](https://github.com/googleapis/python-analytics-data/commit/1e4f58e60668dc590e7c91f9997b9eb2bdf0b948))


### Bug Fixes

* **deps:** require google-api-core>=1.33.1,>=2.8.0 ([1e4f58e](https://github.com/googleapis/python-analytics-data/commit/1e4f58e60668dc590e7c91f9997b9eb2bdf0b948))
* **deps:** require protobuf >= 3.20.1 ([1e4f58e](https://github.com/googleapis/python-analytics-data/commit/1e4f58e60668dc590e7c91f9997b9eb2bdf0b948))

## [0.13.2](https://github.com/googleapis/python-analytics-data/compare/v0.13.1...v0.13.2) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#266](https://github.com/googleapis/python-analytics-data/issues/266)) ([0990dae](https://github.com/googleapis/python-analytics-data/commit/0990daeb180e59855ef7dd4e549ed7fb20d8ecdc))
* **deps:** require proto-plus >= 1.22.0 ([0990dae](https://github.com/googleapis/python-analytics-data/commit/0990daeb180e59855ef7dd4e549ed7fb20d8ecdc))

## [0.13.1](https://github.com/googleapis/python-analytics-data/compare/v0.13.0...v0.13.1) (2022-07-19)


### Documentation

* **samples:** add runFunnelReport sample ([#258](https://github.com/googleapis/python-analytics-data/issues/258)) ([af9d130](https://github.com/googleapis/python-analytics-data/commit/af9d1300e296a60b86f12021c133d2eb7a4f71c1))

## [0.13.0](https://github.com/googleapis/python-analytics-data/compare/v0.12.1...v0.13.0) (2022-07-17)


### Features

* add audience parameter ([c2a27d7](https://github.com/googleapis/python-analytics-data/commit/c2a27d70ae9e3d3aa5213c61546dc1b23b03768a))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#253](https://github.com/googleapis/python-analytics-data/issues/253)) ([c2a27d7](https://github.com/googleapis/python-analytics-data/commit/c2a27d70ae9e3d3aa5213c61546dc1b23b03768a))
* rename the `funnel_filter` field of the `FunnelFilterExpression` type to `funnel_field_filter` ([3ff59b2](https://github.com/googleapis/python-analytics-data/commit/3ff59b2235fc965ce58eb8104b55ea7940264c8f))
* rename the type `FunnelFilter` to `FunnelFieldFilter` ([#251](https://github.com/googleapis/python-analytics-data/issues/251)) ([3ff59b2](https://github.com/googleapis/python-analytics-data/commit/3ff59b2235fc965ce58eb8104b55ea7940264c8f))
* require python 3.7+ ([#255](https://github.com/googleapis/python-analytics-data/issues/255)) ([0b81da4](https://github.com/googleapis/python-analytics-data/commit/0b81da498c6c5acba2d39d794c0a9795f7265342))

## [0.12.1](https://github.com/googleapis/python-analytics-data/compare/v0.12.0...v0.12.1) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#242](https://github.com/googleapis/python-analytics-data/issues/242)) ([94137c5](https://github.com/googleapis/python-analytics-data/commit/94137c50660b9e4236a17c914662ff98ee587fbf))


### Documentation

* fix changelog header to consistent size ([#243](https://github.com/googleapis/python-analytics-data/issues/243)) ([8e65b0d](https://github.com/googleapis/python-analytics-data/commit/8e65b0d89590ebaa611e4106e7b4bff967c95338))

## [0.12.0](https://github.com/googleapis/python-analytics-data/compare/v0.11.2...v0.12.0) (2022-05-07)


### Features

* **v1alpha:** add analytics admin v1alpha ([#239](https://github.com/googleapis/python-analytics-data/issues/239)) ([383e896](https://github.com/googleapis/python-analytics-data/commit/383e89613010bd9a5941b425a78b63dab8eb7deb))


### Documentation

* clarify start_minutes_ago and end_minutes_ago ([#235](https://github.com/googleapis/python-analytics-data/issues/235)) ([45dd51e](https://github.com/googleapis/python-analytics-data/commit/45dd51e7eb9d627064e72159716b72bcd68a9c48))
* fix typo in get_common_metadata.py sample ([#224](https://github.com/googleapis/python-analytics-data/issues/224)) ([7234e84](https://github.com/googleapis/python-analytics-data/commit/7234e84c4a2130b8a6055765867467920debfd8a))
* fixes incorrect comment in python sample ([#220](https://github.com/googleapis/python-analytics-data/issues/220)) ([749e8f2](https://github.com/googleapis/python-analytics-data/commit/749e8f21431dd355bf4547d26b206ecfcf56c509))
* removes unnecessary period in python sample description ([#225](https://github.com/googleapis/python-analytics-data/issues/225)) ([5e363e4](https://github.com/googleapis/python-analytics-data/commit/5e363e4250587cae7601fa90604274d0bf86a1f1))

## [0.11.2](https://github.com/googleapis/python-analytics-data/compare/v0.11.1...v0.11.2) (2022-04-01)


### Documentation

* fixes typo in python sample ([#214](https://github.com/googleapis/python-analytics-data/issues/214)) ([8978387](https://github.com/googleapis/python-analytics-data/commit/8978387b7781439df13db666f0af112ac517144e))

## [0.11.1](https://github.com/googleapis/python-analytics-data/compare/v0.11.0...v0.11.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#202](https://github.com/googleapis/python-analytics-data/issues/202)) ([cc351cd](https://github.com/googleapis/python-analytics-data/commit/cc351cd9d65daf9d6546717cebf212bcb2ddf16e))
* **deps:** require proto-plus>=1.15.0 ([cc351cd](https://github.com/googleapis/python-analytics-data/commit/cc351cd9d65daf9d6546717cebf212bcb2ddf16e))

## [0.11.0](https://github.com/googleapis/python-analytics-data/compare/v0.10.0...v0.11.0) (2022-02-24)


### Features

* add api key support ([#182](https://github.com/googleapis/python-analytics-data/issues/182)) ([ad51ffd](https://github.com/googleapis/python-analytics-data/commit/ad51ffd1c461663d7ff055b69166004ea5a4d686))


### Bug Fixes

* **deps:** delete unused dependency libcst ([#191](https://github.com/googleapis/python-analytics-data/issues/191)) ([dbba912](https://github.com/googleapis/python-analytics-data/commit/dbba91295c9deacca67f8862da628e05cee6c4cc))
* resolve DuplicateCredentialArgs error when using credentials_file ([97804fe](https://github.com/googleapis/python-analytics-data/commit/97804feb1031e3ff6ac3e6f6113b1d3123f1ec91))


### Documentation

* add autogenerated code snippets ([f34ee10](https://github.com/googleapis/python-analytics-data/commit/f34ee10dce4dae5f04aefedf9d8f3472491025d3))

## [0.10.0](https://www.github.com/googleapis/python-analytics-data/compare/v0.9.0...v0.10.0) (2021-11-01)


### Features

* add the `blocked_reasons` field to the `MetricMetadata` type that contains reasons why access was blocked ([583920a](https://www.github.com/googleapis/python-analytics-data/commit/583920a4d0efd8c4c08e9f40379732052773c1d0))
* add the `currency_code`, `time_zone` fields to the `ResponseMetaData` type ([583920a](https://www.github.com/googleapis/python-analytics-data/commit/583920a4d0efd8c4c08e9f40379732052773c1d0))
* add the `empty_reason` field to the `ResponseMetaData` type that contains an empty report reason ([583920a](https://www.github.com/googleapis/python-analytics-data/commit/583920a4d0efd8c4c08e9f40379732052773c1d0))
* add the `schema_restriction_response` field to the `ResponseMetaData` type ([#157](https://www.github.com/googleapis/python-analytics-data/issues/157)) ([583920a](https://www.github.com/googleapis/python-analytics-data/commit/583920a4d0efd8c4c08e9f40379732052773c1d0))


### Bug Fixes

* **deps:** require google-api-core >= 1.28.0 ([1f81d4e](https://www.github.com/googleapis/python-analytics-data/commit/1f81d4eacc5f00bd6666fb4437aed9b78b3cd761))


### Documentation

* list oneofs in docstring ([1f81d4e](https://www.github.com/googleapis/python-analytics-data/commit/1f81d4eacc5f00bd6666fb4437aed9b78b3cd761))

## [0.9.0](https://www.github.com/googleapis/python-analytics-data/compare/v0.8.1...v0.9.0) (2021-10-11)


### Features

* add context manager support in client ([#147](https://www.github.com/googleapis/python-analytics-data/issues/147)) ([4773796](https://www.github.com/googleapis/python-analytics-data/commit/4773796b8f645e26d60b097d7c52c3c84549a759))
* add trove classifier for python 3.9 and python 3.10 ([#150](https://www.github.com/googleapis/python-analytics-data/issues/150)) ([199ab6f](https://www.github.com/googleapis/python-analytics-data/commit/199ab6f2fac2fe4729a2fba36cce2cc5d5ec7bc4))

## [0.8.1](https://www.github.com/googleapis/python-analytics-data/compare/v0.8.0...v0.8.1) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([a9accfd](https://www.github.com/googleapis/python-analytics-data/commit/a9accfd6e61ff2d0c18fdfaea1cf8d4a12671770))

## [0.8.0](https://www.github.com/googleapis/python-analytics-data/compare/v0.7.2...v0.8.0) (2021-09-01)


### Features

* add `category` field to `DimensionMetadata`, `MetricMetadata` types ([81c2eea](https://www.github.com/googleapis/python-analytics-data/commit/81c2eeaf88f8fc5a15a1df13e3fef02437a23bb7))
* add `CheckCompatibility` method to the API ([#131](https://www.github.com/googleapis/python-analytics-data/issues/131)) ([81c2eea](https://www.github.com/googleapis/python-analytics-data/commit/81c2eeaf88f8fc5a15a1df13e3fef02437a23bb7))
* add `DimensionCompatibility`, `MetricCompatibility`, `Compatibility` types to the API ([81c2eea](https://www.github.com/googleapis/python-analytics-data/commit/81c2eeaf88f8fc5a15a1df13e3fef02437a23bb7))

## [0.7.2](https://www.github.com/googleapis/python-analytics-data/compare/v0.7.1...v0.7.2) (2021-07-27)


### Bug Fixes

* enable self signed jwt for grpc ([#114](https://www.github.com/googleapis/python-analytics-data/issues/114)) ([f3861ee](https://www.github.com/googleapis/python-analytics-data/commit/f3861ee3cafb7824b2c80f28b4d6e175cb3d7cfe))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#110](https://www.github.com/googleapis/python-analytics-data/issues/110)) ([6d3c10c](https://www.github.com/googleapis/python-analytics-data/commit/6d3c10cd2cffd98197dc32ce1290f8b2c4289485))


### Miscellaneous Chores

* release as 0.7.2 ([#115](https://www.github.com/googleapis/python-analytics-data/issues/115)) ([3b9e48b](https://www.github.com/googleapis/python-analytics-data/commit/3b9e48bd25a8370c83d6dd82cc406acbfa7cdc2d))

## [0.7.1](https://www.github.com/googleapis/python-analytics-data/compare/v0.7.0...v0.7.1) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#109](https://www.github.com/googleapis/python-analytics-data/issues/109)) ([62e0ee7](https://www.github.com/googleapis/python-analytics-data/commit/62e0ee732cbd915d3630f2526a0591d76b027a3e))

## [0.7.0](https://www.github.com/googleapis/python-analytics-data/compare/v0.6.1...v0.7.0) (2021-07-10)


### Features

* add `minute_ranges` field to `RunRealtimeReportRequest` object  ([#101](https://www.github.com/googleapis/python-analytics-data/issues/101)) ([8523e6a](https://www.github.com/googleapis/python-analytics-data/commit/8523e6ad87f126766576d71b05d68478960bd10b))
* add always_use_jwt_access ([1678019](https://www.github.com/googleapis/python-analytics-data/commit/16780195811dd93333afe6e27b674dd5e78705a3))


### Bug Fixes

* disable always_use_jwt_access ([#97](https://www.github.com/googleapis/python-analytics-data/issues/97)) ([1678019](https://www.github.com/googleapis/python-analytics-data/commit/16780195811dd93333afe6e27b674dd5e78705a3))


### Documentation

* document the increase of the number of allowed dimensions in a report query ([8523e6a](https://www.github.com/googleapis/python-analytics-data/commit/8523e6ad87f126766576d71b05d68478960bd10b))
* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-analytics-data/issues/1127)) ([#87](https://www.github.com/googleapis/python-analytics-data/issues/87)) ([6e30719](https://www.github.com/googleapis/python-analytics-data/commit/6e30719c4158c0e2e7580bff373e94cf7dd91475)), closes [#1126](https://www.github.com/googleapis/python-analytics-data/issues/1126)

## [0.6.1](https://www.github.com/googleapis/python-analytics-data/compare/v0.6.0...v0.6.1) (2021-06-16)


### Bug Fixes

* exclude docs and tests from package ([#82](https://www.github.com/googleapis/python-analytics-data/issues/82)) ([acd60f1](https://www.github.com/googleapis/python-analytics-data/commit/acd60f15ae2192e54b180776b62ee2ea9fce7d3f))

## [0.6.0](https://www.github.com/googleapis/python-analytics-data/compare/v0.5.1...v0.6.0) (2021-06-08)


### Features

* support self-signed JWT flow for service accounts ([ff2beb8](https://www.github.com/googleapis/python-analytics-data/commit/ff2beb8f923570a78772712dc140fc7ba99148d6))


### Bug Fixes

* add async client to %name_%version/init.py ([ff2beb8](https://www.github.com/googleapis/python-analytics-data/commit/ff2beb8f923570a78772712dc140fc7ba99148d6))

## [0.5.1](https://www.github.com/googleapis/python-analytics-data/compare/v0.5.0...v0.5.1) (2021-05-28)


### Bug Fixes

* **deps:** require google-api-core>=1.22.2 ([675ae9f](https://www.github.com/googleapis/python-analytics-data/commit/675ae9fb45bc4ea1adbbba1a302f04daf6368fbf))


### Documentation

* add sample code for Data API v1 ([#57](https://www.github.com/googleapis/python-analytics-data/issues/57)) ([a1e63c5](https://www.github.com/googleapis/python-analytics-data/commit/a1e63c56f5fa5835c528724c9d861c18cb34d6ad))

## [0.5.0](https://www.github.com/googleapis/python-analytics-data/compare/v0.4.1...v0.5.0) (2021-04-01)


### Features

* add `kind` field which is used to distinguish between response types ([#60](https://www.github.com/googleapis/python-analytics-data/issues/60)) ([83f1fc1](https://www.github.com/googleapis/python-analytics-data/commit/83f1fc1af4baa799d3f457127ef2fe687b0aa49d))
* add `potentially_thresholded_requests_per_hour` field to `PropertyQuota` ([83f1fc1](https://www.github.com/googleapis/python-analytics-data/commit/83f1fc1af4baa799d3f457127ef2fe687b0aa49d))


### Documentation

* update quickstart samples to support the Data API v1 beta ([#50](https://www.github.com/googleapis/python-analytics-data/issues/50)) ([ad51cf2](https://www.github.com/googleapis/python-analytics-data/commit/ad51cf28f6c3e306780ca48eb26299b4158068ad))
* update region tag names to match the convention ([#55](https://www.github.com/googleapis/python-analytics-data/issues/55)) ([747f551](https://www.github.com/googleapis/python-analytics-data/commit/747f551c4b3a2f5b3d4602788b8f9c19cbd9904b))

## [0.4.1](https://www.github.com/googleapis/python-analytics-data/compare/v0.4.0...v0.4.1) (2021-03-16)


### Bug Fixes

* fix from_service_account_info for async clients ([#44](https://www.github.com/googleapis/python-analytics-data/issues/44)) ([fdebf9b](https://www.github.com/googleapis/python-analytics-data/commit/fdebf9b96e915a06fecaeb83c1ca59de077249a8))
* **v1beta:** (BREAKING) rename the 'page_size', 'page_token', 'total_size' fields to 'limit', 'offset' and 'row_count' respectively ([8fd57a3](https://www.github.com/googleapis/python-analytics-data/commit/8fd57a340b7e052dc9c4d6c33882add75405eb8b))

## [0.4.0](https://www.github.com/googleapis/python-analytics-data/compare/v0.3.0...v0.4.0) (2021-02-25)


### Features

* add v1beta ([#35](https://www.github.com/googleapis/python-analytics-data/issues/35)) ([8b43efe](https://www.github.com/googleapis/python-analytics-data/commit/8b43efe93086e1846ad68173fac3929492e98e0a))

## [0.3.0](https://www.github.com/googleapis/python-analytics-data/compare/v0.2.0...v0.3.0) (2021-01-06)


### Features

* add custom_definition to DimensionMetadata object and MetricMetadata object ([9bd3477](https://www.github.com/googleapis/python-analytics-data/commit/9bd347737319ea5cae0cf6556d55cd8397a06811))
* add from_service_account_info factory and fix sphinx identifiers  ([#27](https://www.github.com/googleapis/python-analytics-data/issues/27)) ([2775104](https://www.github.com/googleapis/python-analytics-data/commit/2775104b84dda7cccc0fe2813cb8fde5e8930ae8))


### Bug Fixes

* remove client recv msg limit and add enums to `types/__init__.py` ([#22](https://www.github.com/googleapis/python-analytics-data/issues/22)) ([b3dc882](https://www.github.com/googleapis/python-analytics-data/commit/b3dc88221da924816f04e8c0ce716c0d45555d4c))

## [0.2.0](https://www.github.com/googleapis/python-analytics-data/compare/v0.1.0...v0.2.0) (2020-11-16)


### Features

* add support for realtime reports ([#12](https://www.github.com/googleapis/python-analytics-data/issues/12)) ([929c44c](https://www.github.com/googleapis/python-analytics-data/commit/929c44c466fa1cb08255c0be730b2a9d1d2e2c04)), closes [/github.com/googleapis/python-talent/blob/ef045e8eb348db36d7a2a611e6f26b11530d273b/samples/snippets/noxfile_config.py#L27-L32](https://www.github.com/googleapis//github.com/googleapis/python-talent/blob/ef045e8eb348db36d7a2a611e6f26b11530d273b/samples/snippets/noxfile_config.py/issues/L27-L32)


### Documentation

* added a sample ([#7](https://www.github.com/googleapis/python-analytics-data/issues/7)) ([a4bcc31](https://www.github.com/googleapis/python-analytics-data/commit/a4bcc3147efd800b2ef754fe1af27361842e7cdc))

## 0.1.0 (2020-09-14)


### Features

* generate v1alpha1 ([488c410](https://www.github.com/googleapis/python-analytics-data/commit/488c4106c782f55a59c90a4a311e4f6431a1b1c1))
