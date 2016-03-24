
def geojson2ogr(file_base, new_format, name_new_file, path_directory):
    import subprocess
    import os
    kwargs = {
        "file_base": file_base,
        "name_new_file": name_new_file,
        "path_directory": path_directory
    }
    if new_format == "csv":
        command = 'ogr2ogr -f "CSV" {path_directory}{name_new_file}.csv {file_base}'.format(**kwargs)
        filename = "{}.csv".format(name_new_file)
    elif new_format == "kml":
        command = 'ogr2ogr -f "KML" {path_directory}{name_new_file}.kml {file_base}'.format(**kwargs)
        filename = "{}.kml".format(name_new_file)
    elif new_format == "shp":

        command_convert = 'ogr2ogr -f "ESRI Shapefile" {path_directory}{name_new_file}.shp {file_base}'.format(**kwargs)
        command_zip = 'zip -j {path_directory}{name_new_file} {path_directory}{name_new_file}.*'.format(**kwargs)
        if not subprocess.call(command_convert, shell=True):
            os.remove(file_base)
            if not subprocess.call(command_zip, shell=True):
                exclude = [".dbf", ".prj", ".shp", ".shx"]
                for ext in exclude:
                    del_file = path_directory + name_new_file + ext
                    if os.path.exists(del_file):
                        os.remove(del_file)
            else:
                return ''
        else:
            return ''
        filename = "{}.zip".format(name_new_file)
        return filename
    else:
        return ''
    if subprocess.call(command, shell=True):
        return ''
    if os.path.exists(file_base):
        os.remove(file_base)
    return filename
