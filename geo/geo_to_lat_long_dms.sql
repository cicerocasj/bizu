drop function lat_dms_from_geom(geom GEOMETRY);
CREATE OR REPLACE FUNCTION lat_dms_from_geom(geom GEOMETRY)
RETURNS varchar
AS
$$
DECLARE
s text;
BEGIN
	SELECT replace(replace(replace(a[1], ';', ' '), 'W', 'O'), 'L', 'E')::varchar into s FROM (
	    select regexp_split_to_array(ST_AsLatLonText(ST_AsText(geom), 'C;D;M;S.SSSS'), ' ')
	) as dt(a);
	return s;
END;
$$
LANGUAGE plpgsql;
select lat_dms_from_geom(ST_GeometryFromText('POINT(-40.654321 15.123456)', 4326));

drop function lon_dms_from_geom(geom GEOMETRY);
CREATE OR REPLACE FUNCTION lon_dms_from_geom(geom GEOMETRY)
RETURNS varchar
AS
$$
DECLARE
s text;
BEGIN
	SELECT replace(replace(replace(a[2], ';', ' '), 'W', 'O'), 'E', 'L')::varchar into s FROM (
	    select regexp_split_to_array(ST_AsLatLonText(ST_AsText(geom), 'C;D;M;S.SSSS'), ' ')
	) as dt(a);
	return s;
END;
$$
LANGUAGE plpgsql;
select lon_dms_from_geom(ST_GeometryFromText('POINT(-40.654321 15.123456)', 4326));

