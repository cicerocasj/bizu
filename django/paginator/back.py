def pagination(elements, page_selected, interval):
    '''
    params
    elements: list
    page_selected: str
    interval: int
    return: elements of page and list of paginator
    '''
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
    paginator = Paginator(elements, interval)
    page = paginator.num_pages if page_selected == "-1" else int(page_selected)

    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    pages = [{"classe": "disabled" if results.number == 1 else "", "label": "«"}]
    if paginator.num_pages > 10:
        if page > 6 and page < paginator.num_pages - 6:
            for p in xrange(1, 3):
                pages.append({"label": p, "classe": "active" if p == results.number else ""})
            pages.append({"label": "...", "classe": "disabled"})
            for p in xrange(page-3, page+4):
                pages.append({"label": p, "classe": "active" if p == results.number else ""})
            pages.append({"label": "...", "classe": "disabled"})
            for p in xrange(paginator.num_pages-1, paginator.num_pages+1):
                pages.append({"label": p, "classe": "active" if p == results.number else ""})
        elif page <= 6:
            for p in xrange(1, 8):
                pages.append({"label": p, "classe": "active" if p == results.number else ""})
            pages.append({"label": "...", "classe": "disabled"})
            for p in xrange(paginator.num_pages-2, paginator.num_pages+1):
                pages.append({"label": p, "classe": "active" if p == results.number else ""})
        elif page >= paginator.num_pages - 6:
            for p in xrange(1, 3):
                pages.append({"label": p, "classe": "active" if p == results.number else ""})
            pages.append({"label": "...", "classe": "disabled"})
            for p in xrange(paginator.num_pages-8, paginator.num_pages+1):
                pages.append({"label": p, "classe": "active" if p == results.number else ""})
    else:
        for p in paginator.page_range:
            pages.append({"label": p, "classe": "active" if p == results.number else ""})
    pages.append({"classe": "disabled" if results.number == paginator.num_pages else "", "label": "»"})
    return results.o.object_list, pages

